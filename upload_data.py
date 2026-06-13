import os
from pymongo import MongoClient
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB
mongo_db = os.getenv("mongo_db")
client = MongoClient(mongo_db, tls=True, tlsAllowInvalidCertificates=True)
collection = client["sample_mflix"]["personalpdf"]

# Load your PDF
loader = PyPDFLoader("Manoj Nahak Resume 2026.pdf")  # ← put your PDF name here
documents = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)

# Load embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store in MongoDB
print(f"Uploading {len(chunks)} chunks to MongoDB...")

for i, chunk in enumerate(chunks):
    embedding_vector = embedding.embed_query(chunk.page_content)
    
    collection.insert_one({
        "text": chunk.page_content,        # original text
        "embedding": embedding_vector,      # vector for search
        "source": chunk.metadata.get("source", ""),  # file name
        "page": chunk.metadata.get("page", 0)        # page number
    })
    print(f"Uploaded chunk {i+1}/{len(chunks)}")

print("✅ Done! All data uploaded to MongoDB.")