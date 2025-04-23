# AI Resume Skills Scanner

A Flask web application to extract and match skills from uploaded resumes to job descriptions using Natural Language Processing.

## ✨ Features
- Upload resume (PDF/DOCX)
- Extract relevant skills
- Match against job description
- Clean, user-friendly interface

## 📸 Screenshots

### Upload Page
![Upload Page](screenshots/upload_page.png)

### Extracted Skills Output
![Output Result](screenshots/output_result.png)

## 🚀 Getting Started

```bash
git clone https://github.com/vaish59/resume-skills-scanner.git
cd resume-skills-scanner
pip install -r requirements.txt
python app.py


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

🛠️ Tech Stack
Python
Flask
HTML, CSS (Jinja2 templates)
spaCy / nltk

📁 uploads/ Folder
Create an empty uploads/ folder and add a .gitkeep file inside if you want it to stay in the repo (Git doesn’t track empty folders).
touch uploads/.gitkeep