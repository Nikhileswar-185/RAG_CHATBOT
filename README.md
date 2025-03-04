# RAG\_CHATBOT

A **Retrieval-Augmented Generation (RAG)** chatbot built using **Streamlit, LangChain, FAISS, and Hugging Face embeddings**. This chatbot answers user queries based on custom data.

---

## 🚀 Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Nikhileswar-185/RAG_CHATBOT.git
cd RAG_CHATBOT
pip install -r requirements.txt
```

---

## 📂 Data Preparation

Place all your **PDF files** inside the `data` folder. These documents will be used to generate embeddings for retrieval.

---

## 🔑 LLM Configuration

1. **Generate a GEMINI API Key** using the link below and replace it in the `.env` file:

   [Get GEMINI API KEY](https://www.google.com)

2. **Alternative LLM Services**: If you want to use another LLM service, modify the `generate_response()` function in the `llm.py` file accordingly.

---

## 🛠 How to Use

### 1️⃣ Generate Embeddings & Create FAISS Index

Run the following command to process the documents and create the FAISS vector database:

```bash
python create_faiss_index.py
```

Once you see the message **"All files processed successfully!"**, proceed to the next step.

### 2️⃣ Start the Chatbot

Run the following command to launch the chatbot in your browser:

```bash
streamlit run app.py
```

This will start the chatbot interface on **localhost**. Let it load till you see the text box , and you are ready to query on your custom documents
---

## 🤖 Features

✅ **Supports PDF documents as knowledge base**\
✅ **Uses FAISS for efficient similarity search**\
✅ **Retrieval-Augmented Generation (RAG) approach**\
✅ **Easy-to-use Streamlit UI**\
✅ **Configurable with different LLMs**

---

📧 Contact

For any queries, reach out to [Nikhileswar185@gmail.com](mailto\:Nikhileswar185@gmail.com).
