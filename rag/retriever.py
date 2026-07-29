import chromadb
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Connect ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_db"
)


collection = client.get_or_create_collection(
    name="sri_lanka_travel"
)

if collection.count() == 0:
    from rag.vector_store import *



def search_travel(query, results=3):

    # Convert user query into embedding
    query_embedding = model.encode(
        query
    ).tolist()


    # Search vector database
    response = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=results
    )


    return response["documents"][0]



if __name__ == "__main__":


    user_query = """
    I want adventure places in Sri Lanka 
    with budget accommodation
    """


    documents = search_travel(
        user_query
    )


    print("\nRelevant Documents:\n")


    for doc in documents:

        print("--------------------")
        print(doc[:500])