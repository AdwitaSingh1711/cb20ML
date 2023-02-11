from flask import Flask, render_template, request, url_for, Response
from flask_restful import Api, Resource, reqparse
import cv2
import os
from matplotlib import pyplot as plt
import numpy as np
from logging import FileHandler,WARNING
import re
from werkzeug.utils import secure_filename
from OCR import ocr_core


app = Flask(__name__, template_folder='templates')
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads\\')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods = ['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', msg = 'Please select a file')
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', msg = "File isn't present")
        if file and allowed_file(file.filename):
            filename = str(secure_filename(file.filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'])+file.filename)
            extracted = ocr_core(file)
            extension=filename.split(".")
            extension=str(extension[1])
            source=UPLOAD_FOLDER+"/"+filename
            destination=UPLOAD_FOLDER+extracted+"."+extension
            # file.save(UPLOAD_FOLDER+=file.filename)
        	#source=UPLOAD_FOLDER+"/"+file.filename
        	#destination=UPLOAD_FOLDER+"\"+extracted+'.jpg'
            os.rename(source,destination) #renaming the uploaded file
            return render_template('upload.html',
        							extracted = extracted, 
        							img_src = UPLOAD_FOLDER + file.filename)
    else:
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)






'''from flask import Flask, jsonify, request
from Summarisetext import summarize
from OCR import process_image

app = Flask(__name__)
@app.route("/",method=["POST"])

#summary fetching function
def response():
    query=dict(request.form)['query']
    iamge_name = query['image']
    text = process_image(iamge_name)
    result = summarize(text, 1.5)
    return jsonify({
                    'Summary': result,
                    })

if __name__ == "__main__":
    app.run(host="0.0.0.0")'''

'''@app.route("/ocr", methods=["POST"])
def ocr_api():
    image = request.files.get("image")
    image = Image.open(image)
    text = pytesseract.image_to_string(image)
    return jsonify({"text": text})
    
    if __name__ == "__main__":
    app.run(debug=True)'''

'''from flask import Flask, jsonify, request
from Summarisetext import summarize
from OCR import process_image'''

#with open(f'ocr.pkl', 'rb') as f:
#    ocr = pickle.load(f)
#with open(f'summariser.pkl', 'rb') as f:
#    summariser = pickle.load(f)

'''app = Flask(__name__)
@app.route("/",method=["POST"])
def create():
    iamge_name = request.files.get('image')
    text = process_image(iamge_name)
    result = summarize(text, 1.5)
    return jsonify({'Summary': result,})
    
if __name__ == "__main__":
    app.run(debug = True)'''