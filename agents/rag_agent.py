from rag.retriever import search_travel


def rag_agent(destination):

    results = search_travel(destination)

    return {
        "sender": "RAG Agent",
        "destination": destination,
        "travel_information": results
    }


if __name__ == "__main__":

    response = rag_agent("Kitulgala")

    print(response)