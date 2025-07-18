import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

chroma_client = chromadb.Client()
collection = chroma_client.create_collection("chapters", embedding_function=SentenceTransformerEmbeddingFunction("all-MiniLM-L6-v2"))

def store_version(text: str, version_tag: str):
    collection.add(documents=[text], ids=[version_tag])

def semantic_search(query: str, k=2):
    results = collection.query(query_texts=[query], n_results=k)
    return results
