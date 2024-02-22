import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()

st.title("News Research App")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Analyze")
file_path = 'vectorstore_openai.pkl'

# progress bar
main_placeholder = st.empty()

# create llm
llm = OpenAI(temperature=0.9, max_tokens=500)

if process_url_clicked:
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Loading data...")
    data = loader.load()

    # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Splitting data...")
    docs = text_splitter.split_documents(data)

    # create embeddings and save it to FAISS index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Creating embeddings...")
    time.sleep(2)

    # save the FAISS index to a pickle file
    with open(file_path, 'wb') as f:
        pickle.dump(vectorstore_openai, f)

query = main_placeholder.text_input("Enter your question here:")
if query:
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_chain_type(
                llm=llm,
                retriever=vectorstore.as_retriever()
            )
            result = chain({'question': query}, return_only_outputs=True) # formate will be {"answer": "", "sources": []}
            # display answer
            st.header("Answer")
            st.subheader(result['answer'])
            
            # display sources
            sources = result.get('sources', '')
            if sources:
                st.header("Sources")
                sources_list = sources.split('\n')
                for source in sources_list:
                    st.write(source)