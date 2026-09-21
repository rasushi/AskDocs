import chromadb
from sentence_transformers import SentenceTransformer


# Connect to existing ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="askdocs"
)


# Load the same embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# User's question
#query = "CNN encoder decoder attention architecture four encoder levels multi-feature extractor parallel channel attention"
query = "What architecture was used for neural network?"

# Convert question into an embedding
query_embedding = model.encode(query)


# Search ChromaDB
results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=5,
    include=["documents", "distances", "metadatas"]
)


# Display retrieved chunks
for i, document in enumerate(results["documents"][0]):

    print(f"\n--- Result {i + 1} ---")
    print("Distance:", results["distances"][0][i])
    print("Chunk ID:", results["metadatas"][0][i]["chunk_id"])
    print(document)