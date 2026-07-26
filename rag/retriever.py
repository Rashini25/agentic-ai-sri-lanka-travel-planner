import chromadb
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Connect to existing Chroma database
client = chromadb.PersistentClient(
    path="./chroma_db"
)


collection = client.get_collection(
    name="sri_lanka_travel"
)


def search_travel(destination, results=1):

    query = f"Travel information about {destination}"

    # Convert query into embedding
    query_embedding = model.encode(
        query
    ).tolist()


    # Search similar documents
    response = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=results
    )


    return response["documents"][0]


if __name__ == "__main__":

    query = "adventure activities in Sri Lanka"


    results = search_travel(query)


    print("\nRelevant Documents:\n")


    for result in results:
        print("----------------")
        print(result[:300])