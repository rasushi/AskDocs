from loader import extract_text
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from sentence_transformers import SentenceTransformer

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

print(len(embeddings))
print(embeddings.shape)