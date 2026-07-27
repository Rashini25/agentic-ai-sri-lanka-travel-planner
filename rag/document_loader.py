import os


def load_documents(folder_path):
    documents = []

    for root, dirs, files in os.walk(folder_path):

        for filename in files:

            if filename.endswith(".txt"):

                file_path = os.path.join(root, filename)

                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                documents.append({
                    "filename": filename,
                    "path": file_path,
                    "content": content
                })

    return documents


if __name__ == "__main__":

    docs = load_documents("data")

    print("Total documents loaded:", len(docs))

    for doc in docs[:3]:
        print("\n---")
        print(doc["filename"])