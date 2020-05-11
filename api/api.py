from flask import Flask
from flask import request
from flask import jsonify
from ImageUtilities import saveToPNG
from classify import Classify

app = Flask(__name__)

@app.route('/submit', methods = ['POST'])
def get_image_data():
    dat = request.form['javascript_data']
    saveToPNG(dat)
    pred = Classify('image2.png')
    return str(pred)