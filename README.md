# 🧠 Resume Skill Matcher (Flask App)

This web app lets you upload a resume (PDF) and a job description, then checks how well they match based on skills using NLP.

## 🔧 Features

- Extracts skills from resumes
- Compares with job description
- Displays match percentage
- Clean, beautiful web interface

## 🚀 How to Run Locally

1. Clone this repo:
git clone https://github.com/your-username/resume-skill-matcher.git
cd resume-skill-matcher
Create a virtual environment (optional but recommended):


python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies:


pip install -r requirements.txt
python -m spacy download en_core_web_sm
Run the app:

python app.py
Go to http://127.0.0.1:5000 in your browser.

📁 Folder Structure
lua
resume-skill-matcher/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── result.html
└── uploads/

🛠 Tech Stack
Python (Flask)
PyPDF2
spaCy
HTML/CSS (no JS required)

---

## 📦 `requirements.txt`

```txt
Flask
PyPDF2
spacy
📁 uploads/ Folder
Create an empty uploads/ folder and add a .gitkeep file inside if you want it to stay in the repo (Git doesn’t track empty folders).
touch uploads/.gitkeep