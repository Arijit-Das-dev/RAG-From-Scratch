from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_chroma import Chroma

# Targeted DataBase where all the searches will be done
target_db = "db/ChromaDB"


# Setting up embedding model
embedding_model = HuggingFaceBgeEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

# Setting up the embedding model + targeted DB
db = Chroma(

    persist_directory=target_db,
    embedding_function=embedding_model,
    collection_metadata={"hnsw:space":"cosine"}
)


# User query
query = "What are Tensor Processing Units (TPUs) designed for?"


# Top-k [3] relevent chunks
retriever = db.as_retriever(
    search_kwargs = {"k":3}
)


relevent_docs = retriever.invoke(query)
print(f" User query : {query}")


for i, doc in enumerate(relevent_docs, 1):

    print(f"Document : {i}")
    print("\nCONTENT")
    print(f"\n {doc.page_content}")