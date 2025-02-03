import os
from datetime import datetime
from dotenv import load_dotenv
from google.cloud import aiplatform
import numpy as np
import chromadb
from sentence_transformers import SentenceTransformer

load_dotenv()

# Initialize ChromaDB
client = chromadb.PersistentClient(path="./chroma_db2")
collection = client.get_or_create_collection("dialogues")

# Load a larger embedding model
model = SentenceTransformer("thenlper/gte-large")

# Add dialogues
dialogues = ["Hello, how are you?", "What is your name?", "Tell me a joke."]
embeddings = model.encode(dialogues).tolist()

for i, dialogue in enumerate(dialogues):
    collection.add(ids=[str(i)], embeddings=[embeddings[i]], documents=[dialogue])

# Search for similar dialogues
query = "Who are you?"
query_embedding = model.encode([query]).tolist()
results = collection.query(query_embeddings=query_embedding, n_results=3)

# Print the closest dialogues
print(results)
