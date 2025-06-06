from flask import Flask, render_template, request
import os
from pdf_reader import extract_text_from_pdf
from extractors import extract_email, extract_phone, extract_skills, extract_name, extract_experience
from database import init_db, insert_data, fetch_all
from utils import SKILL_LIST, SKIP_KEYWORDS

app = Flask(__name__)
UPLOAD_FOLDER = 'resumes'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize DB
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_data = None
    verification_result = None

    if request.method == 'POST':
        if 'resume' not in request.files:
            return "No file part", 400
        file = request.files['resume']
        job_qualifications = request.form.get('job_qualifications', '').strip()

        if file.filename == '':
            return "No selected file", 400
        if file and file.filename.lower().endswith('.pdf'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            raw_text = extract_text_from_pdf(filepath)
            name = extract_name(raw_text)
            email = extract_email(raw_text)
            phone = extract_phone(raw_text)
            skills = extract_skills(raw_text, SKILL_LIST)
            experience = extract_experience(raw_text)

            insert_data(name, email, phone, skills, experience)

            extracted_data = {
                "Name": name,
                "Email": email,
                "Phone": phone,
                "Skills": skills,
                "Experience": experience
            }

        else:
            return "Only PDF files allowed", 400

    all_data = fetch_all()

    return render_template('index.html',
                           extracted=extracted_data,
                           all_data=all_data,
                           verification=verification_result
                           )

if __name__ == '__main__':
    app.run(debug=True)
