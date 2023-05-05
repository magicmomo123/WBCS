from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import numpy as np 
import ast
import json
from scipy.io.wavfile import write
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


global out 
out = []
global i 
i = 0
global saved 
saved = 0
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.config['UPLOAD_FOLDER'] = 'static/files'

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():
    form = FlaskForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        data, rate = read_wav_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        output(data, out)
        
    return render_template('index.html', form=form)

@app.route('/upload')
def upload():
    form = UploadFileForm()
    return render_template('upload.html', form=form)

def read_wav_file(file_path):
    rate, data = read(file_path)
    if data.ndim > 1:
        data = np.mean(data, axis=1)
    return data, rate

def output(frame, out):
    for i in frame:
        out.append(i)
    if (len(out) > 10000):
        out = np.array(out)
        plt.plot(out[:100])
        plt.savefig('plot.png')
        write('sound2.wav', 38400, 100*out.astype(np.int32))
        out.clear()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
