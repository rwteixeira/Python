import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Construir as funcionalidades
@app.route('/')
def homepage():
    return '<h1>A API está operacional!</h1>'

@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('advertising.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)

# Rodar a api
app.run()
