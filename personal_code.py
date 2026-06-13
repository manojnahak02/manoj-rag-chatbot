import os
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from pymongo import MongoClient
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import streamlit as st
import os

# Load from Streamlit secrets
groq_api = st.secrets["groq_api"]
mongo_db = st.secrets["mongo_db"]
print(groq_api,mongo_db)
# Set API key for Groq
os.environ["GROQ_API_KEY"] = groq_api
# load_dotenv()

# os.environ["GROQ_API_KEY"] = os.getenv("groq_api")
# mongo_db = os.getenv("mongo_db")

if not os.getenv("GROQ_API_KEY"):
    print("GROQ_API_KEY is not set in environment variables.")
else:
    print("GROQ_API_KEY is set.")

if not mongo_db:
    print("MONGO_DB_URI is not set in environment variables.")
else:
    print("MONGO_DB_URI is set.")


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,
    max_tokens=1000,
)

# Connect to your MongoDB deployment

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

client = MongoClient(
    mongo_db,
    tls=True,
    tlsAllowInvalidCertificates=True,
    serverSelectionTimeoutMS=5000
)

collection =  client["sample_mflix"]["personalpdf"]

def get_query_results(query):
  """Gets results from a vector search query."""

  query_embedding = embedding.embed_query(query)
  pipeline = [
      {
            "$vectorSearch": {
              "index": "vector_index",
              "queryVector": query_embedding,
              "path": "embedding",
              "numCandidates":384,
              "limit": 10
            }
        }, {
            "$project": {
              "_id": 0,
              "text": 1
         }
      }
  ]

  results = collection.aggregate(pipeline)

  array_of_results = []
  for doc in results:
      array_of_results.append(doc)

  return array_of_results

def llm_response(query):
    context_docs = get_query_results(query)
    context_string = " ".join([doc["text"] for doc in context_docs])
    
    prompt = f"""Use the following pieces of context to answer the question at the end.
    {context_string}
    please read the question carefully and answer based on the above context. If the question cannot be answered using the above context, say you don't know.
    Question: {query}
    """
    
    response = llm.invoke(prompt)
    return response.content

