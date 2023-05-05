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
class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        #file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        file.save('/Users/aryanallanthighall/Documents/FlaskECE445/static/files/mp3.mp3')
    return render_template('index.html', form = form)


@app.route('/adc', methods = ['GET', 'POST'])
def data():
    data = request.data
    
    #print(type(json.loads(data)))
    data = json.loads(data)
    output(data, out, saved)
    return render_template('data.html')

def output(frame, out, saved):
    #print('out', type(out))
    #print('frame', type(frame))

    for i in frame :
        out.append(i)
    #print(out)
    if (len(out) > 10000):
        if (saved == 0):
            
            out = np.array(out)
            plt.plot(out[:100])
            plt.savefig('plot.png')
            #issue is typecasting 
            write('sound2.wav', 38400, 100*out.astype(np.int32))
            saved = 1
if __name__ == "__main__":

    app.run(debug = True, host='0.0.0.0',port=5001)
