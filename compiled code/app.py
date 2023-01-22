from flask import Flask, jsonify, request
from PIL import Image
import pytesseract
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

#ocr

def process_image(iamge_name):
    text = pytesseract.image_to_string(Image.open(iamge_name))
    return text

#summariser

def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
    document= nlp(text)
    tokenizing=[token.text for token in document]
    word_frequencies={}
    for word in document:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in document.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    return summary

#flask app

app = Flask(__name__)
@app.route("/",method=["POST"])
def create():
    #query=dict(request.form)['query']
    #iamge_name = query['image']
    iamge_name = request.files.get('image')
    text1 = process_image(iamge_name)
    result = summarize(text1, 1.5)
    return jsonify({'Summary': result,})
    
if __name__ == "__main__":
    app.run(debug = True)