from flask import Flask, redirect, url_for, request, render_template
from requests import get

app = Flask(__name__)

@app.route('/')
def paginaInicial() :
    return render_template('inicio.html')

@app.route('/acesso/')
def fazerLogin() :
    return render_template('login.html')

@app.route('/welcome/')
def welcome() :
    return render_template('welcome.html')

@app.route('/pagina403')
def pagina403() :
    return render_template('pagina403.html')

@app.validador()
def validade() :
    return render_template
    

if __name__ == "__main__" :
    app.run(debug=True)