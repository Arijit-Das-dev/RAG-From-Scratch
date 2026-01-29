import google.generativeai as genai
from dotenv import load_dotenv
import os


class GeminiEmbeddings:

    def __init__(self, model = "models/embedding-001"):
        
        load_dotenv()
        self.model = model
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    # Chunks to embeddings
    def embed_documents(self, texts):
        embeddings = []
        for text in texts:
            response = genai.embed_content(
                model=self.model,
                content=text,
                task_type="retrieval_document"
            )
            embeddings.append(response["embedding"])
        return embeddings

    # User query to embeddings
    def embed_query(self, text):
        response = genai.embed_content(
            model=self.model,
            content=text,
            task_type="retrieval_query"
        )
        return response["embedding"]