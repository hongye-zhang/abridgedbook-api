
from flask import Flask, request
import shutil
import os
import supabase

app = Flask(__name__)


@app.route('/uploadpdf', methods=['POST'])
def upload_pdf():
    # check if the post request has the file part
    if 'file' not in request.files:
        return {"detail": "No file part in request."}, 400

    file = request.files['file']

    # if no file is selected
    if file.filename == '':
        return {"detail": "No selected file."}, 400

    if not file.filename.endswith(".pdf"):
        return {"detail": "Invalid file type. PDF file expected."}, 400

    if file:
        filename = file.filename
        #file_path = os.path.join(os.getcwd(), filename)

        return {"filename": filename, "message": "File saved locally."}, 200


@app.route('/')
def hello_world():
    return 'Hello, World!'