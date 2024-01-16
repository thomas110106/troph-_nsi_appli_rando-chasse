from flask import Flask, render_template, request, session, redirect, url_for
import json
from os.path import join, dirname, realpath

app = Flask(__name__)

app.config['DATA_DIR'] = join(dirname(realpath(__file__)),'static')
app.secret_key = b'99b45274a4b2da7440ab249f17e718688b53b646f3dd57f23a9b29839161749f'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/log_chasseur")
def log_chasseur():
    return render_template('log_chasseur.html')

@app.route("/carte")
def carte():
    return render_template('carte.html')
 
app.run(host = '127.0.0.1', port='8080', debug=True)