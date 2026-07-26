import chromadb
from sentence_transformers import SentenceTransformer

from document_loader import load_documents


# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Create ChromaDB storage
client = chromadb.PersistentClient(
    path="./chroma_db"
)


collection = client.get_or_create_collection(
    name="sri_lanka_travel"
)


# Load travel documents
documents = load_documents(
    "data/travel_documents"
)


texts = []
ids = []


for index, doc in enumerate(documents):

    texts.append(
        doc["content"]
    )

    ids.append(
        doc["filename"]
    )


# Convert text into embeddings
embeddings = model.encode(
    texts
).tolist()


# Store documents
collection.add(
    documents=texts,
    embeddings=embeddings,
    ids=ids
)


print(
    "Documents stored successfully:",
    len(documents)
)