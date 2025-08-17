🐳☸ DevOps RAG AI Agent

A smart AI assistant for Docker & Kubernetes that helps DevOps engineers quickly diagnose issues, suggest fixes, and provide step-by-step guidance. Built with Gemini AI, Python, and Streamlit, this project combines RAG (Retrieval-Augmented Generation) with conversational memory for accurate, context-aware responses.

🚀 Live Demo

Try the app online:
Try it Now →

🛠 Features

🔍 Instant Issue Diagnosis: Paste logs or describe your problem, and get step-by-step solutions.

📂 Contextual Answers: AI answers are based on your documents and previous conversation.

💬 Conversation History: Maintains session history to provide context-aware follow-ups.

🐳☸ Docker & Kubernetes Support: Focused guidance for containerized environments.

⚡ Fast & Interactive: Built with Streamlit for an interactive UI.

📁 Getting Started
Prerequisites

Python 3.10+

Gemini API Key

Installation
git clone https://github.com/gk-anonymous/Devops_RAG_Agent.git
cd Devops_RAG_Agent
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt

Usage

Create a .env file in the root directory:

GEMINI_API_KEY=your_gemini_api_key_here


Run the Streamlit app:

streamlit run main.py


Open the local URL provided by Streamlit and start diagnosing your Docker/Kubernetes issues.

📂 Project Structure
Devops_RAG_Agent/
│
├─ data/               # Text files used for AI context
├─ main.py             # Streamlit app & AI logic
├─ requirements.txt    # Python dependencies
├─ .env                # Gemini API Key (not committed)
├─ .gitignore          # Ignore venv, .env, etc.
└─ README.md

💡 Usage Example

Paste logs or type your question:

Q: How do I fix Kubernetes pod restarts?


Get AI-generated answer:

A: Check the pod events using kubectl describe pod...


Follow step-by-step guidance. The chat history keeps track of previous questions and answers.

🌐 Tech Stack

Python & Streamlit (Frontend & UI)

Gemini AI (LLM & Embeddings)

NumPy (Vector calculations)

RAG (Retrieval-Augmented Generation)

🔒 Security

API keys stored in .env (never committed).

.gitignore includes venv/ and .env for security.

📈 Future Improvements

Add multi-file support for larger logs.

Integrate Slack/Teams bot for DevOps notifications.

Add code snippet suggestions for automation tasks.

⭐ Contributing

Feel free to fork the repository, submit issues, or open pull requests!

Live Demo: https://devopsragagent-mtpwmqrkxn2drsmvvm2rnw.streamlit.app/
