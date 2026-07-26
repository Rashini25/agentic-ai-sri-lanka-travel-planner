from rag.retriever import search_travel


def get_travel_information(query):

    results = search_travel(
        query,
        results=3
    )

    return results


if __name__ == "__main__":

    info = get_travel_information(
        "best adventure places in Sri Lanka"
    )

    for item in info:
        print("----------------")
        print(item)