# News Research App
This is an app for news analysis which has the ability to answer any questions related to given news.

## Description

This Streamlit-based application empowers you to explore news articles, delve into their content, and uncover insights using an intelligent retrieval-based question-answering (RQA) system. Leveraging OpenAI's language models and vector embeddings, the app helps you extract meaning from news articles and answer your questions with relevant information.

## Features:

- **Intuitive UI**: Streamlit's user-friendly interface makes it easy to feed in news article URLs and pose your questions.
- **Powerful Retrieval Engine**: The app utilizes FAISS (Facebook AI Similarity Search) to efficiently search through article text and find relevant passages.
- **OpenAI Language Models**: OpenAI's language models generate well-structured and informative answers based on retrieved information.
- **Source Citations**: The app provides links to the original news articles, ensuring transparency and enabling further exploration.

## Getting Started

1. **Prerequisites**: Ensure you have `Python 3.x`, `Streamlit`, `langchain`, `dotenv`, and `OpenAI API` credentials installed.
2. **Set up OpenAI API Key**: Create an account on OpenAI and obtain your API key. Store it securely in a `.env` file using the following format:
```
OPENAI_API_KEY=your_api_key
```
3. **Clone or download**: Obtain the project's code repository.
4. **Run the app**: Execute `streamlit run main.py` in the project directory.

## How it Works

1. **Enter News Article URLs**: Use the text input fields in the sidebar to add URLs of news articles you want to explore.
2. **Analyze**: Click the "Analyze" button to process the articles and create an internal search index.
3. **Ask Your Question**: Once the analysis is complete, type your question in the main input field.
4. **Get Answers**: The app will retrieve relevant passages from the articles and generate a comprehensive answer using OpenAI's language models. You'll also see the original article links for reference.

## Customization

- You can modify the number of URLs allowed in the sidebar.
= Adjust the text splitter configuration in `langchain.text_splitter.RecursiveCharacterTextSplitter` to control how documents are divided into smaller chunks.
- Fine-tune the OpenAI language model settings (e.g., temperature, max tokens) for more specific answer generation.
- Explore advanced customization options provided by the `langchain` library.

## Additional Notes

- This project is for educational and research purposes. Please use it responsibly and ethically.
- Consider improving the app's error handling and providing more detailed guidance for customization.
- Share your experience and feedback to help the project grow!