# !/usr/bin/env python
# coding: utf-8
from flask import Flask, render_template, request, url_for, session
from flask_session import Session
from database.perguntas import perguntas

app = Flask(__name__, template_folder='templates')

SESSION_TYPE = 'filesystem'
app.config["SESSION_PERMANENT"] = False
app.config.from_object(__name__)
Session(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
   

@app.route('/nome', methods=['GET', 'POST'])
def nome():
    data = request.form.to_dict() 
    session['nome'] = data.get('nome') 
    session['temp'] = 'Ariella'
    app.logger.info(data)
    return render_template('nome.html', data=data)

def calcula(resultado):
    cont = 0
    for resposta in resultado.values():
        if resposta == "True":
            cont +=1
    return cont

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    nome = session['nome']
    data = request.form.to_dict() 
    cont = calcula(data)
    app.logger.info(data)
    return render_template('formulario.html', perguntas = perguntas, cont = cont, nome=nome)


app.run(port=5000, host='localhost', debug=True)