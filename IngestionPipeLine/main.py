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

def main():

    print("Main Function")
    


if __name__ == "__main__":

    main()