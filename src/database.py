import json
import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

db = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding
)

def load_data():
    with open("data/sports_facts.json", "r") as file:
        sports_data = json.load(file)

    if len(db.get()["ids"]) > 0:
        print("Data already exists")
        return

    documents = []

    for item in sports_data:
        documents.append(
            Document(
                page_content=item["fact"],
                metadata={"sport": item["sport"]}
            )
        )

    db.add_documents(documents)

    print("Data inserted into ChromaDB")


def search_data(sport):
    results = db.similarity_search(
        query=sport,
        k=3,
        filter={"sport": sport}
    )

    return [doc.page_content for doc in results]