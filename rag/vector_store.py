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


# Create or connect to collection
collection = client.get_or_create_collection(
    name="sri_lanka_travel"
)


# Load all Sri Lanka travel documents
documents = load_documents(
    "data"
)


texts = []
ids = []
metadatas = []


# Prepare documents for vector database
for index, doc in enumerate(documents):

    texts.append(
        doc["content"]
    )

    # Use unique path as ID
    ids.append(
        doc["path"]
    )

    # Add metadata for better retrieval
    metadatas.append(
        {
            "filename": doc["filename"],
            "source": doc["path"]
        }
    )


# Convert text into embeddings
embeddings = model.encode(
    texts
).tolist()


# Store documents in ChromaDB
collection.add(
    documents=texts,
    embeddings=embeddings,
    ids=ids,
    metadatas=metadatas
)


print(
    "Documents stored successfully:",
    len(documents)
)