import os
from flask import Flask,render_template
from app.day import current_day

app = Flask(__name__)

@app.route('/')
def index():
    p = current_day()

    return render_template('index.html',n=p)
