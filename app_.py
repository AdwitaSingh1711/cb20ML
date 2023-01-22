from flask import Flask, jsonify, request
from Summarisetext import summarize
from OCR import process_image

#with open(f'ocr.pkl', 'rb') as f:
#    ocr = pickle.load(f)
#with open(f'summariser.pkl', 'rb') as f:
#    summariser = pickle.load(f)

app = Flask(__name__)
@app.route("/",method=["POST"])
def create():
    iamge_name = request.files.get('image')
    text = process_image(iamge_name)
    result = summarize(text, 1.5)
    return jsonify({'Summary': result,})
    
if __name__ == "__main__":
    app.run(debug = True)