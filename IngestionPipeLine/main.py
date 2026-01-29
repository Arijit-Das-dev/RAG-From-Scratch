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

def load_all_files(file_path = "Docs"):

    print(f"LOADING ALL THE FILES FROM {file_path}")

    if not os.path.exists(file_path): 

        raise FileNotFoundError(f"{file_path} DOES NOT EXISTS")
    
    loader = DirectoryLoader(

        path=file_path,
        glob="*.txt",
        loader_cls=TextLoader
    )
    
    print("_______FILE LOADED SUCCESSFULLY_______")

    # Loading all the documents [.txt] from Docs folder
    documents = loader.load()

    if len(documents) == 0:

        raise FileNotFoundError(f"{file_path} CONTAINS NOTHING. ENSURE THAT FILE IS NOT EMPTY.")
    
    for i, doc in documents[:1]:

        print(f"File no. {i+1}")

    return documents


def main():

    print("Main Function")



if __name__ == "__main__":

    main()