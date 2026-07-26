import os


def load_documents(folder_path):
    documents = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):

            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            documents.append({
                "filename": filename,
                "content": content
            })

    return documents


if __name__ == "__main__":

    docs = load_documents(
        "data/travel_documents"
    )

    print("Total documents loaded:", len(docs))

    for doc in docs[:3]:
        print("\n---")
        print(doc["filename"])