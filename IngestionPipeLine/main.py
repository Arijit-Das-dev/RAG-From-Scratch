import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

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
    
    # Loading the Folder
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
    
    for i, doc in enumerate(documents[:1]):

        print(f"\nFile no. {i+1}")
        print(f" \nSource: {doc.metadata['source']}")
        print(f" \ncontent length: {len(doc.page_content)} characters")
        print(f" \ncontent preview: {doc.page_content[:100]}...")
        print(f" \nmetadata: {doc.metadata}")

    return documents


def main():

    print("Main Function")

    document = load_documents(file_path="Docs")

    print(document)

if __name__ == "__main__":

    main()
    