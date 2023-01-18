from flask import Flask, jsonify, request
from Summarisetext import summarize
from OCR import process_image

app = Flask(__name__)
@app.route("/summariser",method=["POST"])

#summary fetching function
def response():
    query=dict(request.form)['query']
    iamge_name = query['image']
    text = process_image(iamge_name)
    per = query['percent']
    result = summarize(text, per)
    return jsonify({
                    'Summary': result,
                    })

if __name__ == "__main__"
    app.run(host="0.0.0.0")