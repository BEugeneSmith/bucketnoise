import os
from flask import Flask,render_template,url_for
from app.day import current_date

app = Flask(__name__)

@app.route('/')
def index():
    p = current_date()
    print (p[-1])

    return render_template('index.html',n=p)

@app.route('/about')
def about():

    return render_template('about.html')
