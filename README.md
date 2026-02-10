<p align="center"> <!-- Core Language --> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <!-- RAG Framework --> <img src="https://img.shields.io/badge/LangChain-000000?style=for-the-badge"/> <!-- Document Loaders --> <img src="https://img.shields.io/badge/PyPDFLoader-00599C?style=for-the-badge"/> <img src="https://img.shields.io/badge/DirectoryLoader-4B8BBE?style=for-the-badge"/> <!-- Text Chunking --> <img src="https://img.shields.io/badge/Text%20Splitter-2C2D72?style=for-the-badge"/> <!-- Embeddings --> <img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"/> <img src="https://img.shields.io/badge/BGE%20Embeddings-0A0A0A?style=for-the-badge"/> <!-- Vector Database --> <img src="https://img.shields.io/badge/ChromaDB-FF6F00?style=for-the-badge"/> <!-- LLM Inference --> <img src="https://img.shields.io/badge/Groq-FF4F00?style=for-the-badge"/> <img src="https://img.shields.io/badge/LLaMA-0467DF?style=for-the-badge"/> <!-- Frontend --> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/> <!-- Utilities --> <img src="https://img.shields.io/badge/Pydantic-0E1A2B?style=for-the-badge"/> <img src="https://img.shields.io/badge/Dotenv-ECD53F?style=for-the-badge"/> <img src="https://img.shields.io/badge/Logging-3A3A3A?style=for-the-badge"/> </p>

# 📌 What is Retrieval-Augmented Generation (RAG)?

Retrieval-Augmented Generation (RAG) is an advanced AI architecture that combines information retrieval with Large Language Models (LLMs) to generate more accurate, factual, and context-aware responses.

Instead of relying only on the model’s internal knowledge, RAG systems retrieve relevant information from external data sources (documents, PDFs, databases, APIs, etc.) and use that retrieved context to guide the LLM’s generation.
<br>
# This approach significantly reduces:

1. Hallucinations ❌

2. Outdated answers ❌

3. Lack of domain knowledge ❌
<br>
# 🧠 Why RAG is Important ?

Traditional LLMs:

i) Are trained on static data

ii) Cannot access private or real-time knowledge

iii) Often hallucinate answers
<br>
# RAG systems:

→ Work with custom & private data

→ Support real-time updates

→ Produce grounded, verifiable outputs

→ Are used in production AI systems
<br>
# RAG is widely used in:

1. Chatbots & AI assistants

2. Enterprise knowledge bases

3. Document Q&A systems

4. AI search engines

5. Customer support automation
<br>
# ⚙️ Core Components of a RAG System

# Data Source :
PDFs, text files, web pages, databases, APIs, etc.

# Chunking & Preprocessing
Documents are split into smaller chunks for better retrieval.

# Embedding Model
Converts text chunks into vector embeddings.

# Vector Database
Stores embeddings and enables fast similarity search
(FAISS, Chroma, Pinecone, Weaviate, etc.)

# Retriever
Fetches the most relevant chunks based on user queries.

# LLM (Generator)
Uses retrieved context + user query to generate final answers.
<br>
# 🔁 RAG Workflow (High Level)

1. User asks a question

2. Query is converted into embeddings

3. Relevant documents are retrieved from the vector database

4. Retrieved context is injected into the LLM prompt

5. LLM generates a grounded response
<br>

# 🎯 Goal of This Repository

• This repository is a hands-on learning journey focused on:

• Understanding RAG concepts from scratch

• Building RAG pipelines step by step

• Experimenting with embeddings, retrievers, and LLMs

• Exploring real-world, production-oriented RAG workflows

• The repo evolves gradually from basic RAG concepts → advanced systems, following an industry-aligned approach.

## 📚 Learning Resources & References
- 🎥 [RAG Fundamentals & Core Concepts](https://youtu.be/63B-3rqRFbQ?si=dBMJoo5MA43XkwiD)
- 🎥 [LLM + RAG Architecture Overview](https://youtu.be/9iGvXxH_fdE?si=ACJvQI-zLAf-zMvR)
- 🎥 [LLM + RAG Architecture Overview (Extended)](https://youtu.be/9iGvXxH_fdE?si=ACJvQI-zLAf-zMvR)
- 🎥 [Document Ingestion Pipeline Design](https://youtu.be/brbd3AvsJWs?si=RaNiBN-jK1uLcLp1)
- 🎥 [Chunking Strategies for RAG](https://youtu.be/nbJVJ1RPBEg?si=gmvhT1hASqvye-ht)
- 🎥 [Embeddings Explained for Semantic Search](https://youtu.be/i_v4Vm2KBuc?si=AMtDBUNxrqqUz-rB)
- 🎥 [Vector Databases & Similarity Search](https://youtu.be/ZWXXpK4TIDY?si=SoKB-ne8jcEf04Ti)
- 🎥 [Retriever Design & Top-K Selection](https://youtu.be/POE8LDjdAw4?si=yJ3P8-Yt35ZXknM8)
- 🎥 [Context Window & Prompt Engineering](https://youtu.be/Ht8ImZT6kJ0?si=6XfJZ3eZnF2e6FyU)
- 🎥 [LLM Inference Optimization](https://youtu.be/FPYtGK6HYRg?si=FnDuUwrBSxf1d6Sm)
- 🎥 [End-to-End RAG Implementation](https://youtu.be/slG8qWvIPKg?si=PEGHZMHp4OWbmNuD)
- 🎥 [RAG Failure Modes & Debugging](https://youtu.be/dHgvDTXVvPA?si=g7OnO9HP96X7SWx5)
- 🎥 [Production-Ready RAG Patterns](https://youtu.be/kNU-J4NNNhk?si=ICpPmHcf4eQL8d_D)
- 🎥 [Scaling RAG Systems](https://youtu.be/1qQCuWiRIfA?si=C5MumrVdP-g4RouL)
