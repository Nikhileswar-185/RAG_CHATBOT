# RAG\_CHATBOT

A **Retrieval-Augmented Generation (RAG)** chatbot built using **Streamlit, LangChain, FAISS, and Hugging Face embeddings**. This chatbot can answer user queries based on custom data.

---

## 🚀 Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Nikhileswar-185/RAG_CHATBOT.git
cd RAG_CHATBOT
pip install -r requirements.txt
```

---

## 🔑 LLM Configuration

To use **Gemini API**[Free of charge one], create an API key and add it to the `.env` file.

🔗 [Get GEMINI API KEY](https://www.google.com)

- If you want to use a different LLM service, modify the `generate_response()` function in the **LLM class** located in `llm.py` accordingly.

---

## 📖 How to Use

Run the following commands in the terminal:

### **1️⃣ Create FAISS Embeddings**

```bash
python create_faiss_index.py
```

Once you see the message **"All files processed successfully!"**, proceed to the next step.

### **2️⃣ Start the Chatbot**

```bash
streamlit run app.py
```

This will launch the chatbot on **localhost**.
Let it load till you see the text box , and you are ready to query on your custom documents
---


## 📧 Contact

For any queries, reach out to [**Nikhileswar185@gmail.com**](mailto\:your-email@example.com).

---

