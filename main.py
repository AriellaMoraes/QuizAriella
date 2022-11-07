# !/usr/bin/env python
# coding: utf-8
from flask import Flask, render_template, request, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

app.run(port=5000, host='localhost', debug=True)