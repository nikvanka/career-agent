# 🤖 AI Career Mentor Agent

An Agentic AI-powered career assistant that analyzes resumes against job descriptions, identifies skill gaps, suggests improvements, generates personalized learning roadmaps, and creates interview questions.

## 🚀 Features

### Resume Analysis

* Extracts skills, projects, strengths, and weaknesses
* Identifies missing keywords and technologies

### Job Description Analysis

* Understands job requirements
* Extracts required technical and soft skills

### Skill Gap Detection

* Compares resume with job requirements
* Highlights matching and missing skills

### Learning Roadmap

* Generates a personalized learning plan
* Recommends technologies and topics to study

### Interview Preparation

* Technical interview questions
* HR interview questions
* Scenario-based questions

---

## 🏗️ Architecture

```text
User
  │
  ▼
Streamlit UI
  │
  ▼
Career Mentor Agent
  │
  ├── Resume Analyzer
  ├── Job Description Analyzer
  ├── Skill Gap Analyzer
  ├── Learning Roadmap Generator
  └── Interview Question Generator
  │
  ▼
Results Dashboard
```

---

## 🛠️ Tech Stack

| Component              | Technology    |
| ---------------------- | ------------- |
| Frontend               | Streamlit     |
| LLM                    | Google Gemini |
| Framework              | LangChain     |
| PDF Processing         | PyPDF         |
| Environment Management | Python Dotenv |
| Version Control        | Git & GitHub  |

---

## 📂 Project Structure

```text
career-agent/
│
├── app.py
├── agents.py
├── rag.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/career-agent.git
cd career-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Get your API key from Google AI Studio.

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📋 Usage

1. Upload your resume (PDF)
2. Paste a job description
3. Click **Analyze**
4. Review:

   * Skill Gap Report
   * Resume Suggestions
   * Learning Roadmap
   * Interview Questions

---

## 🎯 Future Enhancements

* ChromaDB Vector Database
* RAG-based Knowledge Retrieval
* Multi-Agent Architecture (CrewAI)
* LangGraph Workflows
* Job Recommendation Engine
* ATS Score Calculator
* Resume Rewriter
* GitHub Profile Analyzer
* LinkedIn Profile Review

---

## 📸 Example Use Cases

### Students

* Internship preparation
* Placement readiness
* Resume improvement

### Job Seekers

* Resume optimization
* Skill gap analysis
* Interview preparation

### Career Switchers

* Learning roadmap generation
* Technology transition planning

---

## 🌟 Agentic AI Concepts Demonstrated

* Large Language Models (LLMs)
* Prompt Engineering
* Agent Design
* Tool Usage
* Resume Intelligence
* Career Guidance Automation

---

## 👨‍💻 Author

Nikhil Vanka

Engineering Student | AI & Agentic AI Enthusiast

GitHub: https://github.com/nikvanka
