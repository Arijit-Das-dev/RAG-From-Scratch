import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma


"""
Steps =>

1. Load all the files
2. Chunk the files
3. Embedded and storing it in VectorDB

"""

# loading all the files
def load_documents(file_path = "Docs"):

    print(f"\n\nLOADING ALL THE FILES FROM {file_path}")

    if not os.path.exists(file_path): # Checking if the folder path exists or not

        raise FileNotFoundError(f"{file_path} DOES NOT EXISTS") # if not exist then raise FileNotFoundError
    

    # Selecting the folders and files inside it
    loader = DirectoryLoader( # If exist then load the [folder + files] into the LangChain Directory

        path=file_path,
        glob="*.txt",
        loader_cls=TextLoader
    )
    
    print("_______FILE LOADED SUCCESSFULLY_______")

    # Loading Folders to the LangChain Directory
    documents = loader.load()

    if len(documents) == 0: # If the documents is empty then raise FileNotFoundError

        raise FileNotFoundError(f"{file_path} CONTAINS NOTHING. ENSURE THAT FILE IS NOT EMPTY.") # Error
    
    for i, doc in enumerate(documents[:1]): # We are selecting only the first file inside that folder => "Docs"

        print(f"\nFile no. {i+1}")
        print(f" \nSource: {doc.metadata['source']}") # File location/Name
        print(f" \ncontent length: {len(doc.page_content)} characters") # total characters inside the text file
        print(f" \ncontent preview: {doc.page_content[:100]}...") # Printing only the first 100 characters from the file
        print(f" \nmetadata: {doc.metadata}")

    return documents


# Splitting the documents files into chunks
def split_documents(document, chunk_size=800, chunk_overlap=0):

    print("Spliting all the documents into chunks")

    # Splitting All the texts
    text_splitter = CharacterTextSplitter(

        chunk_size=chunk_size, # splitted upto 800 chars 
        chunk_overlap=chunk_overlap 
    )

    # We are assigning all the splitted texts inside each chunks
    chunks = text_splitter.split_documents(document)

    if chunks:

        for i, chunk in enumerate(chunks[:6]):

            print(f" \nChunk : {i+1}")
            print(f" \nSource : {chunk.metadata['source']}") # Location 
            print(f" \nLength : {len(chunk.page_content)} characters") # How many characters inside the chunk
            print(f" \nContent:")
            print(f" \n{chunk.page_content}") # Chunk Contents
            print("_"*50)

    return chunks


# Getting ready the embeddings and the vectorDB

def create_and_persist_chroma_db(chunks, db_path="dbChromaDB"):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=db_path,
        collection_metadata={"hnsw:space": "cosine"}
    )

    print("____SUCCESSFULL_____")
    return vector_store
    

# main function
def main():

    print("\n____________Main Function____________\n")

    document = load_documents(file_path="Docs")

    splitted_chunks = split_documents(document)

    vector_db = create_and_persist_chroma_db(splitted_chunks)

    print(vector_db)
    

if __name__ == "__main__":

    main()
    