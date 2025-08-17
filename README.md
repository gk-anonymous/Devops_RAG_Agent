# 🐳☸ DevOps RAG AI Agent

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://devopsragagent-mtpwmqrkxn2drsmvvm2rnw.streamlit.app/)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A smart AI assistant for Docker & Kubernetes that helps DevOps engineers quickly diagnose issues, suggest fixes, and provide step-by-step guidance. Built with Gemini AI, Python, and Streamlit, this project combines RAG (Retrieval-Augmented Generation) with conversational memory for accurate, context-aware responses.

![DevOps RAG Agent Demo](https://via.placeholder.com/800x400?text=DevOps+RAG+Agent+Demo+Screenshot)

## 🚀 Live Demo

Try the app online:  
👉 [https://devopsragagent-mtpwmqrkxn2drsmvvm2rnw.streamlit.app/](https://devopsragagent-mtpwmqrkxn2drsmvvm2rnw.streamlit.app/)

## 🛠 Features

| Feature | Description |
|---------|-------------|
| 🔍 **Instant Issue Diagnosis** | Paste logs or describe your problem, get step-by-step solutions |
| 📂 **Contextual Answers** | AI responses based on your documents and conversation history |
| 💬 **Conversation Memory** | Maintains session history for context-aware follow-ups |
| 🐳 **Docker Support** | Specialized troubleshooting for container environments |
| ☸ **Kubernetes Expertise** | Focused guidance for K8s clusters and deployments |
| ⚡ **Interactive UI** | Streamlit-powered interface for smooth user experience |

## 📦 Installation

### Prerequisites
- Python 3.10+
- [Gemini API Key](https://ai.google.dev/)

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/gk-anonymous/Devops_RAG_Agent.git
cd Devops_RAG_Agent

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo "GEMINI_API_KEY=your_api_key_here" > .env

🖥 Usage
bash
streamlit run main.py
Then open the local URL provided by Streamlit (typically http://localhost:8501)

🗂 Project Structure
text
Devops_RAG_Agent/
│
├── data/               # Text files used for AI context
├── main.py             # Streamlit app & AI logic
├── requirements.txt    # Python dependencies
├── .env                # Gemini API Key (not committed)
├── .gitignore          # Ignore venv, .env, etc.
└── README.md
💡 Example Usage
User Question:
"How do I fix Kubernetes pod restarts?"

AI Response:

First check pod events:

bash
kubectl describe pod <pod-name>
Common causes:

Resource limits being hit

Liveness probe failures

OOM (Out of Memory) errors

Next steps:

Examine logs with kubectl logs <pod-name>

Check resource usage with kubectl top pod

The chat history maintains context for follow-up questions.

🌐 Tech Stack
https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white
https://img.shields.io/badge/Streamlit-FF4B4B?logo=Streamlit&logoColor=white
https://img.shields.io/badge/Gemini_AI-4285F4?logo=google&logoColor=white
https://img.shields.io/badge/RAG-Retrieval_Augmented_Generation-green

Frontend: Streamlit

AI Engine: Gemini AI (LLM & Embeddings)

Vector Processing: NumPy

Architecture: Retrieval-Augmented Generation (RAG)

🔒 Security
API keys stored in .env (excluded via .gitignore)

Virtual environment excluded from version control

No persistent storage of sensitive data

🚧 Future Improvements
Multi-file log analysis support

Slack/Teams bot integration

Automated remediation code snippets

Support for additional cloud providers

Performance optimization for large documents

🤝 Contributing
Contributions are welcome! Please:

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE for more information.
