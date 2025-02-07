

from flask import Flask, request, render_template, jsonify
import os
import PyPDF2
from werkzeug.utils import secure_filename

app = Flask(__name__)


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'txt'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

# def generate_interview_questions(resume_text, job_description):
#     questions = []
#     if "Python" in resume_text and "developer" in job_description.lower():
#         questions.extend([
#             "What are Python's key features?",
#             "Explain how Python manages memory.",
#             "Describe your experience with Flask or other web frameworks."
#         ])
#     if "Machine Learning" in resume_text:
#         questions.extend([
#             "Can you explain a recent machine learning project you worked on?",
#             "What are the key differences between supervised and unsupervised learning?"
#         ])
#     if not questions:
#         questions.append("Tell us about your experience with the listed skills.")

#     return questions

def generate_interview_questions(resume_text, job_description):
    questions = []

    # Python-related questions
    if "Python" in resume_text and ("developer" in job_description.lower() or "Python" in job_description.lower()):
        questions.extend([
            "What are Python's key features?",
            "Explain how Python manages memory.",
            "Describe your experience with Flask or other web frameworks."
        ])

    # Machine Learning-related questions
    if "Machine Learning" in resume_text and ("Machine Learning" in job_description.lower() or "AI" in job_description.lower()):
        questions.extend([
            "Can you explain a recent machine learning project you worked on?",
            "What are the key differences between supervised and unsupervised learning?"
        ])

    # JavaScript and Node.js-related questions
    if ("JavaScript" in resume_text and "Node.js" in resume_text) and ("JavaScript" in job_description.lower() or "Node.js" in job_description.lower()):
        questions.extend([
            "Can you explain a project where you used JavaScript and Node.js?",
            "Describe your experience with Express.js and how you have used it in your projects."
        ])

    # Data Structures and Algorithms-related questions
    if ("Data Structure" in resume_text and "Algorithms" in resume_text) and ("Data Structures" in job_description.lower() or "Algorithms" in job_description.lower()):
        questions.extend([
            "How do you approach problem-solving when working with Data Structures and Algorithms?",
            "Can you discuss a challenging bug you encountered while coding and how you resolved it?"
        ])

    # IoT-related questions
    if "IoT" in resume_text and "IoT" in job_description.lower():
        questions.extend([
            "Can you explain your experience with IoT technologies?",
            "Describe the Smart Doorbell project you worked on and the challenges you faced."
        ])

    # Web Development-related questions
    if ("HTML" in resume_text and "CSS" in resume_text and "JavaScript" in resume_text) and ("Web Development" in job_description.lower() or "Frontend" in job_description.lower()):
        questions.extend([
            "Can you walk us through the development of your portfolio website?",
            "What challenges did you face while working on the AgriChain project, and how did you overcome them?"
        ])

    # Soft Skills-related questions
    if ("Leadership" in resume_text or "Communication Skills" in resume_text) and ("Leadership" in job_description.lower() or "Communication" in job_description.lower()):
        questions.extend([
            "Can you describe a situation where you demonstrated leadership skills?",
            "How do you handle communication within a team during a project?"
        ])

    # Default question if no specific skills match
    if not questions:
        questions.append("Tell us about your experience with the listed skills.")

    return questions
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['resume']
    job_description = request.form.get('job_description', '')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

       
        resume_text = extract_text_from_pdf(file_path)

       
        questions = generate_interview_questions(resume_text, job_description)

        return jsonify({'questions': questions})

    return jsonify({'error': 'Invalid file format'}), 400

if __name__ == '__main__':
    app.run(debug=True)