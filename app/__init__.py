from flask import Flask,render_template
from app.scale import *
from random import choice

app = Flask(__name__)

@app.route('/')
def index():
    s = choice(PITCHES)
    m = choice(MODES)

    name = scale(s,m)

    return render_template('index.html',n=name.scale_name)
