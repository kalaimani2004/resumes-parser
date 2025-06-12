# 📄 Resume Parser using AI & NLP

A smart web application that extracts candidate details like **Name, Email, Phone, Skills**, and **Experience Summary** from uploaded PDF resumes. It uses **Python, Flask**, and **Large Language Models (LLMs)** like **Ollama** for enhanced parsing and summarization. Built with a clean Bootstrap UI and extendable architecture.

---

## 🚀 Features

- ✅ Upload PDF resumes via web interface
- ✅ Extracts:
  - Name
  - Email
  - Phone
  - Skills (as bullet points)
  - AI-generated Experience Summary
- ✅ Attractive Bootstrap 5 UI
- ✅ Parsed resume history table
- ✅ Optional: Qualification matching and summary generator using LLMs
- ✅ Local model support via [Ollama](https://ollama.com/)

---

## 🛠️ Tech Stack

| Layer      | Tools Used                   |
|------------|------------------------------|
| Frontend   | HTML, CSS, Bootstrap         |
| Backend    | Python, Flask                |
| AI Engine  | Ollama / GPT (local LLM)     |
| NLP        | SpaCy, Regex, NER            |
| PDF Parser | PyMuPDF or pdfminer.six      |
| Database   | SQLite or PostgreSQL (optional) |

---

## 📦 Setup Instructions

### 🔧 Prerequisites

- Python 3.9+
- pip
- [Ollama](https://ollama.com/download) (if using LLM for experience summary)

### 💻 Installation

```bash
git clone https://github.com/<your-username>/resume-parser.git
cd resume-parser
pip install -r requirements.txt
