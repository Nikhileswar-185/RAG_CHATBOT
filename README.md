# RAG_CHATBOT 
A Retrieval-Augmented Generation (RAG) chatbot built using Streamlit, LangChain, FAISS, and Hugging Face embeddings.  
This chatbot can answer user queries based on our custom data.

## 🚀 Installation  
Clone the repository and install the required dependencies.

```bash
git clone https://github.com/Nikhileswar-185/RAG_CHATBOT.git
cd RAG_CHATBOT
pip install -r requirements.txt


---

## **3️⃣ How to Use**
```md
## 📖 Usage  
1.Run create_faiss_index.py file - it creates embeddings and store them in FAISS vector database
    ```bash
    python create_faiss_index.py
    # Once you see the message "All files processed successfully!"

2. Run the chatbot application:
   ```bash
   streamlit run app.py



