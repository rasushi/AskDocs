from loader import extract_text
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from sentence_transformers import SentenceTransformer
import chromadb

text = extract_text("C:\\Users\\sayye\\Desktop\\AskDocs\\data\\retinal segmentation.pdf")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

documents = []

for i, chunk in enumerate(chunks):
    document = Document(
        page_content=chunk,
        metadata={
            "source": "retinal segmentation.pdf",
            "chunk_id": i
        }
    )

    documents.append(document)

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(
    [doc.page_content for doc in documents]
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="askdocs"
)


# 6. Create IDs
ids = [str(i) for i in range(len(documents))]


# 7. Store everything in ChromaDB
collection.add(
    ids=ids,
    documents=[doc.page_content for doc in documents],
    metadatas=[doc.metadata for doc in documents],
    embeddings=embeddings.tolist()
)


print("Documents added to ChromaDB!")
print("Number of documents:", collection.count())