import os
import glob
import numpy as np
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()  # Load .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("Please set GEMINI_API_KEY in your .env file!")
    st.stop()

# -----------------------------
# Gemini setup
# -----------------------------
genai.configure(api_key=GEMINI_API_KEY)
MODEL = "gemini-2.5-pro"
EMBED = "models/text-embedding-004"

# -----------------------------
# Load & prepare documents
# -----------------------------
docs = []
for f in glob.glob("data/*.txt"):
    with open(f, "r", encoding="utf-8") as file:
        docs.append({"file": f, "text": file.read()})

def split_text(text, size=200):
    words = text.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words), size)]

chunks = []
for d in docs:
    for ch in split_text(d["text"]):
        chunks.append({"file": d["file"], "text": ch})

def embed_text(t):
    r = genai.embed_content(model=EMBED, content=t)
    return np.array(r["embedding"], dtype="float32")

vecs = np.vstack([embed_text(c["text"]) for c in chunks])
vecs = vecs / (np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-8)

def search(query, k=3):
    qv = embed_text(query)
    qv = qv / (np.linalg.norm(qv) + 1e-8)
    sims = vecs @ qv
    idx = np.argsort(-sims)[:k]
    return [chunks[i] for i in idx]

# -----------------------------
# Conversational Gemini function
# -----------------------------
def ask_gemini_conversational(query, history, k=3):
    top = search(query, k)
    doc_context = "\n\n".join(c["text"] for c in top)

    # Build chat history context
    chat_context = ""
    for turn in history:
        chat_context += f"Q: {turn['query']}\nA: {turn['answer']}\n"

    prompt = f"""
Answer only from the document context and previous conversation.
Document context:
{doc_context}

Previous conversation:
{chat_context}

Current question:
{query}
Answer like a DevOps expert, step-by-step.
"""
    model = genai.GenerativeModel(MODEL)
    return model.generate_content(prompt).text

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="🐳☸ DevOps AI Assistant", layout="wide")
st.title("🐳☸ DevOps AI Assistant")
st.markdown("**Docker + Kubernetes Troubleshooter** powered by Gemini AI")

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_area("💡 Describe your issue or paste logs here:", height=150)

if st.button("🔍 Diagnose / Ask"):
    if query.strip() == "":
        st.warning("Please enter your problem/logs")
    else:
        with st.spinner("Analyzing..."):
            answer = ask_gemini_conversational(query, st.session_state.history)
            st.session_state.history.append({"query": query, "answer": answer})

# Display chat history
st.subheader("💬 Conversation History")
for turn in st.session_state.history:
    st.markdown(f"**Q:** {turn['query']}")
    st.markdown(f"**A:** {turn['answer']}")
    st.markdown("---")
