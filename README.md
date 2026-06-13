<<<<<<< HEAD
# 🤖 Manoj RAG Chatbot

An intelligent **Retrieval-Augmented Generation (RAG)** chatbot that delivers accurate, context-aware answers by leveraging custom knowledge stored in MongoDB.

Built using **LangChain, Groq LLM, HuggingFace Embeddings, and Streamlit**, this project demonstrates a complete end-to-end **GenAI pipeline**, combining semantic search with high-speed inference to create a scalable and interactive chatbot experience.

---

## 🚀 Features

- 🔍 Semantic search using vector embeddings  
- 🧠 Context-aware responses with LLM  
- ⚡ Fast inference via Groq (GPT-OSS-120B)  
- 🗄️ MongoDB Atlas vector search integration  
- 💬 Interactive chatbot UI with chat history  
- 💡 Predefined smart suggestions  

---

## 🔄 Flow

1. User enters a query in Streamlit UI  
2. Query is converted into embedding  
3. MongoDB performs vector similarity search  
4. Top relevant documents are retrieved  
5. Context + query passed to LLM  
6. LLM generates final response  

---

## ⚙️ Tech Stack

| Component        | Technology |
|----------------|-----------|
| LLM            | Groq (GPT-OSS-120B) |
| Embeddings     | sentence-transformers (MiniLM) |
| Vector DB      | MongoDB Atlas |
| Framework      | LangChain |
| Frontend       | Streamlit |
| Language       | Python |

---

## 📁 Project Structure

```
manoj-rag-chatbot/
│
├── personal_code.py
├── streamlit_runner.py
├── requirements.txt
├── .env.example
├── .streamlit/
│   └── config.toml
├── manoj_image.jpg
└── README.md
```

---

## 🧠 Core Logic

- Query embedding using HuggingFace model  
- MongoDB `$vectorSearch` for similarity retrieval  
- Context injection into prompt  
- Response generation using Groq LLM  

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```
groq_api=your_groq_api_key
mongo_db=your_mongodb_connection_string
```

---

## 📦 Installation

```bash
git clone https://github.com/your-username/manoj-rag-chatbot.git
cd manoj-rag-chatbot
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run streamlit_runner.py
```

---

## 💡 Example Questions

- Who is Manoj Nahak?  
- Which company he worked at?  
- What work he did at Saregama India Limited & Colgate Palmolive?  
- List GitHub projects  
- Explain vectorless RAG  

---

## 📊 MongoDB Vector Index

```json
{
  "fields": [
    {
      "type": "vector",
      "numDimensions": 384,
      "path": "embedding",
      "similarity": "cosine"
    }
  ]
}
```

---

## ⚠️ Notes

- Ensure `.env` variables are properly set  
- MongoDB cluster must support vector search  
- Groq API key is required  

---

## 🔮 Future Enhancements

- 📄 PDF/document upload support  
- 🧠 Conversation memory  
- 🌐 Deployment (AWS / Streamlit Cloud)  
- 🔐 Authentication system  

---

## 👨‍💻 Author

**Manoj Nahak**  
Aspiring Data Scientist | Machine Learning Engineer  

---
=======
# manoj-rag-chatbot
My RAG chatbot
>>>>>>> 9e7fa0ecb3df34dfc2609a9356efaf6bee310d5f
