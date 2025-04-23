import os
from flask import Flask, request, render_template
from PyPDF2 import PdfReader
import spacy

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

nlp = spacy.load("en_core_web_sm")

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

SKILLS = [
    'python', 'numpy', 'pandas', 'sklearn', 'matplotlib',
    'seaborn', 'tensorflow', 'keras', 'pytorch',
    'machine learning', 'deep learning', 'nlp',
    'computer vision', 'mysql', 'mongodb', 'flask', 'django',
    'aws', 'gcp', 'azure', 'docker'
]

def extract_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_skills(text):
    lower_text = text.lower()
    return [skill for skill in SKILLS if skill in lower_text]

def match_skills(resume_skills, job_desc_text):
    matched = [skill for skill in resume_skills if skill in job_desc_text]
    if not resume_skills:
        return 0, []
    score = len(matched) / len(SKILLS) * 100
    return score, matched

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    resume_file = request.files['resume']
    job_desc = request.form['jobdesc']

    if resume_file and resume_file.filename.endswith('.pdf'):
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
        resume_file.save(resume_path)
    else:
        return "Please upload a valid PDF file."

    resume_text = extract_text(resume_path)
    resume_skills = extract_skills(resume_text)
    match_percent, matched_skills = match_skills(resume_skills, job_desc.lower())

    return render_template('result.html', match=round(match_percent, 2), matched_skills=matched_skills)

if __name__ == '__main__':
    app.run(debug=True)

