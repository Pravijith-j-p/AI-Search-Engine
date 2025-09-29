# AI-Powered Wikipedia Search & Recommendation Engine

## 🚀 Project Overview
This project is a **scalable search and recommendation system** built on a **25GB Simple English Wikipedia dataset**.  
It combines **keyword-based BM25 search**, **semantic vector embeddings**, and **hybrid ranking** to deliver **highly relevant search results**.  

The system demonstrates:  
- **Large-scale document indexing**  
- **Semantic search with embeddings**  
- **Hybrid ranking for relevance**  
- **Search API for integration with UI**  
- **Optional personalization & recommendation layer**  

---

## 🏗️ Architecture (High-Level Design)

![Architecture Diagram]

**Flow:**  

<img width="2042" height="1366" alt="image" src="https://github.com/user-attachments/assets/6a68603e-5dd3-4fc1-9ebd-bb530f38d8b4" />

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI / Flask  
- **Search & Indexing:** BM25 (Whoosh / rank_bm25), FAISS for embeddings  
- **Embeddings:** OpenAI / HuggingFace models  
- **Frontend / Dashboard:** Streamlit / Next.js  
- **Version Control:** Git + GitHub  

---

## 📂 Project Structure

- **Backend:** Python, FastAPI / Flask  
- **Search & Indexing:** BM25 (Whoosh / rank_bm25), FAISS for embeddings  
- **Embeddings:** OpenAI / HuggingFace models  
- **Frontend / Dashboard:** Streamlit / Next.js  
- **Version Control:** Git + GitHub

# 📂 Project Structure

AI-Search-Engine/
│── data/ # Local Wikipedia dataset (not in repo)

│── src/

│ ├── loader.py # Document loading & preprocessing

│ ├── indexer.py # BM25 & embedding indexing

│ ├── api.py # REST API endpoints

│ └── recommender.py # Personalization & ranking

│── notebooks/ # Experiments & prototyping

│── requirements.txt

│── README.md

│── .gitignore



---

## ⚡ Features

1. **Keyword & semantic search**  
2. **Hybrid ranking** (BM25 + embeddings)  
3. **FastAPI/Flask API** for integration  
4. **Optional personalization** with user history  
5. **Scalable architecture** suitable for large datasets  

---

## 🔧 Setup & Installation

```bash
# Clone the repo
git clone https://github.com/Pravijith-j-p/AI-Search-Engine.git
cd AI-Search-Engine

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Place dataset locally
# data/ folder should contain AllCombined.txt

