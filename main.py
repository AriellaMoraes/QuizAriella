# !/usr/bin/env python
# coding: utf-8
from flask import Flask, render_template, request, url_for
from database.perguntas import perguntas

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/nome', methods=['GET', 'POST'])
def nome():
    data = request.form.to_dict() 
    app.logger.info(data)
    return render_template('nome.html', nome=data)

def calcula(resultado):
    cont = 0
    for resposta in resultado.values():
        if resposta == "True":
            cont +=1
    return cont

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    data = request.form.to_dict() 
    cont = calcula(data)
    app.logger.info(data)
    return render_template('formulario.html', perguntas = perguntas, cont = cont)


app.run(port=5000, host='localhost', debug=True)