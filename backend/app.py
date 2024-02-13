from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS from flask_cors
from ResumeParser import ResumeParser
from utils import Utils

try:
    resume = ResumeParser()
except KeyError as e:
    print(f'error from loading ResumeParser{e}')


app = Flask(__name__)
# Allow requests from 'http://localhost:3000' to the '/make_recommendations' route
CORS(app, origins=["*"])

@app.route('/')
def hello():
    return 'Hello, World!'




@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_files = request.files.getlist('files')
    personal_skill = {}
    if len(uploaded_files) == 0:
        return 'No files were uploaded', 400
    
    for file in uploaded_files:
        # Save the file to a desired location
        file.save(f'files/{file.filename}')
        
        # Determine the file type and read it accordingly
        file_path = f'files/{file.filename}'
        if file.filename.lower().endswith('.pdf'):
            text = Utils.read_pdf(file_path)
        elif file.filename.lower().endswith('.txt'):
            text = Utils.read_text(file_path)
        elif file.filename.lower().endswith('.docx'):
            text = Utils.read_docx(file_path)
        else:
            # Handle unsupported file types
            return f'Unsupported file type: {file.filename}', 400
        
        # Process the text further as needed
        skillset = resume.identify_personal_skills(text)
        evaluation = resume.evaluate(skillset)
        personal_skill[file.filename] = evaluation
        
    
    return jsonify(personal_skill)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
