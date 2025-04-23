'''import os
import re
from flask import Flask, request, render_template
from PyPDF2 import PdfReader

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Skill keywords
SKILLS = [
    'python', 'numpy', 'pandas', 'sklearn', 'matplotlib',
    'seaborn', 'tensorflow', 'keras', 'pytorch',
    'machine learning', 'deep learning', 'nlp',
    'computer vision', 'mysql', 'mongodb', 'flask', 'django',
    'aws', 'gcp', 'azure', 'docker'
]

# Extract text from PDF
def extract_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Extract name and skills from resume text
def parse_text(original_text):
    name = "Candidate"
    lines = [line.strip() for line in original_text.split('\n') if line.strip()]

    # Try to find name in first few lines
    for line in lines[:10]:  # Only check first few lines
        if re.match(r'^([A-Z][a-z]+\s){1,3}[A-Z][a-z]+$', line):
            if not any(skip in line.lower() for skip in ['resume', 'cv', 'india', 'maharashtra', 'latur']):
                name = line
                break

    lower_text = original_text.lower()
    skills = [skill for skill in SKILLS if skill in lower_text]

    return {"name": name.title(), "skills": skills}

# Skill match scoring
def match_skills(resume_skills, job_desc_text):
    matched_skills = [skill for skill in resume_skills if skill in job_desc_text]
    if not resume_skills:
        return 0, []
    score = len(matched_skills) / len(SKILLS) * 100
    return score, matched_skills

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Submit route
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
    resume_data = parse_text(resume_text)
    match_percent, matched_skills = match_skills(resume_data["skills"], job_desc.lower())

    return render_template('result.html',
                           name=resume_data["name"],
                           match=round(match_percent, 2),
                           matched_skills=matched_skills)

if __name__ == '__main__':
    app.run(debug=True)

import spacy
nlp = spacy.load("en_core_web_sm")

def parse_text(original_text):
    name = "Candidate"
    doc = nlp(original_text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break

    lower_text = original_text.lower()
    skills = [skill for skill in SKILLS if skill in lower_text]

    return {"name": name.title(), "skills": skills}'''
'''import os
import re
from flask import Flask, request, render_template
from PyPDF2 import PdfReader
import spacy

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Define skill keywords
SKILLS = [
    'python', 'numpy', 'pandas', 'sklearn', 'matplotlib',
    'seaborn', 'tensorflow', 'keras', 'pytorch',
    'machine learning', 'deep learning', 'nlp',
    'computer vision', 'mysql', 'mongodb', 'flask', 'django',
    'aws', 'gcp', 'azure', 'docker'
]

# Function to extract text from PDF
def extract_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to extract name and skills from resume
def parse_text(original_text):
    name = "Candidate"
    doc = nlp(original_text)

    # Debug: Print the first portion of the resume
    print("----- Extracted Text Preview -----")
    print(original_text[:1000])
    print("----------------------------------")

    # Try Spacy to detect name
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            print(f"Spacy PERSON detected: {ent.text}")
            if 2 <= len(ent.text.split()) <= 3:
                name = ent.text.strip()
                break

    # Fallback to regex if Spacy fails or misfires
    if name.lower() == "candidate" or not re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+', name):
        lines = [line.strip() for line in original_text.split('\n') if line.strip()]
        for line in lines[:10]:
            if re.match(r'^([A-Z][a-z]+\s){1,3}[A-Z][a-z]+$', line) and not any(word in line.lower() for word in ['resume', 'cv']):
                print(f"Fallback name detected: {line}")
                name = line.strip()
                break

    # Skill matching
    lower_text = original_text.lower()
    skills = [skill for skill in SKILLS if skill in lower_text]

    return {"name": name.title(), "skills": skills}

# Skill matching logic
def match_skills(resume_skills, job_desc_text):
    matched_skills = [skill for skill in resume_skills if skill in job_desc_text]
    if not resume_skills:
        return 0, []
    score = len(matched_skills) / len(SKILLS) * 100
    return score, matched_skills

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Form submission route
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
    resume_data = parse_text(resume_text)
    match_percent, matched_skills = match_skills(resume_data["skills"], job_desc.lower())

    return render_template('result.html',
                           name=resume_data["name"],
                           match=round(match_percent, 2),
                           matched_skills=matched_skills)

if __name__ == '__main__':
    app.run(debug=True)'''
'''import os
import re
from flask import Flask, request, render_template
from PyPDF2 import PdfReader
import spacy

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Skill keywords
SKILLS = [
    'python', 'numpy', 'pandas', 'sklearn', 'matplotlib',
    'seaborn', 'tensorflow', 'keras', 'pytorch',
    'machine learning', 'deep learning', 'nlp',
    'computer vision', 'mysql', 'mongodb', 'flask', 'django',
    'aws', 'gcp', 'azure', 'docker'
]

# Extract text from PDF
def extract_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Extract name and skills from resume
def parse_text(original_text):
    name = "Candidate"
    doc = nlp(original_text)

    # Debug: print preview of the text
    print("----- Extracted Text Preview -----")
    print(original_text[:1000])
    print("----------------------------------")

    # Skip patterns like URLs and social handles
    skip_patterns = ['linkedin', 'github', 'http', 'www', '.com']

    # Try Spacy to detect PERSON
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            if not any(skip in ent.text.lower() for skip in skip_patterns):
                print(f"Spacy PERSON found: {ent.text}")
                name = ent.text.strip()
                break

    # Fallback to regex if needed
    if name.lower() == "candidate" or not re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+', name):
        lines = [line.strip() for line in original_text.split('\n') if line.strip()]
        for line in lines[:10]:
            if not any(skip in line.lower() for skip in skip_patterns):
                if re.match(r'^([A-Z][a-z]+\s){1,2}[A-Z][a-z]+$', line):
                    print(f"Fallback regex matched name: {line}")
                    name = line.strip()
                    break

    # Extract skills
    lower_text = original_text.lower()
    skills = [skill for skill in SKILLS if skill in lower_text]

    return {"name": name.title(), "skills": skills}

# Match resume skills with job description
def match_skills(resume_skills, job_desc_text):
    matched_skills = [skill for skill in resume_skills if skill in job_desc_text]
    if not resume_skills:
        return 0, []
    score = len(matched_skills) / len(SKILLS) * 100
    return score, matched_skills

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Submit route
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
    resume_data = parse_text(resume_text)
    match_percent, matched_skills = match_skills(resume_data["skills"], job_desc.lower())

    return render_template('result.html',
                           name=resume_data["name"],
                           match=round(match_percent, 2),
                           matched_skills=matched_skills)

if __name__ == '__main__':
    app.run(debug=True)'''
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

