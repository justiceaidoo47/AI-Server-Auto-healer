# 🤖 AI-Powered Server Auto-Healer

A Python automation tool that detects server errors and uses Groq's Llama 3.1 AI to diagnose and suggest fixes in real-time.

## 🚀 Features

- ✅ Reads system error logs (simulated or real)
- ✅ Analyzes errors using Groq AI (Llama 3.1 70B) – **100% free!**
- ✅ Suggests exact terminal commands to fix the issue
- ✅ Saves structured JSON reports for auditing and tracking
- ✅ Secure API key management with `.gitignore`
- ✅ Handles errors gracefully (never crashes)

## 🛠️ Tech Stack

| Category  Technology 
|----------------------
| Language | Python 3.9+ 
| AI Model | Groq Llama 3.1 70B (free tier) 
| Cloud Ready | AWS (S3, EC2 - ready to integrate) 
| OS | Linux / Windows / macOS 

## 📸 Sample Output



## 📂 Project Structure
AI-Server-Auto-Healer/
├── main.py # Main automation script
├── requirements.txt # Python dependencies
├── .env # Your secret API key (ignored by Git)
├── .gitignore # Protects secrets from being uploaded
└── reports/ # Generated JSON reports (ignored by Git)


## 🔧 Setup Instructions

### 1. Clone the repository
bash
git clone https://github.com/justiceaidoo47/AI-Server-Auto-healer.git
cd AI-Server-Auto-healer



#create virtual environment.#
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


#install dependecies#
pip install -r requirements.txt




#set up your API_KEY #
GROQ_API_KEY=gsk_your_real_api_key_here








#RUN THE SCRIPT#
python main.py


