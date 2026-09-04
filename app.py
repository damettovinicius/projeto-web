from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

print(__name__)

@app.route('/')
def inicio():
    return '<h1>0iiiiiii </h1>'

@app.route('/sobre')
def sobre():
    return'''
<h1 style='color:red'>Meu nome é; </h1>
<p>Vinicius Vieira <b>Dametto</b>
<!--LEMBRA DO HTML, SEU BURRO-->
'''
@app.route('/curso')
def curso():
    return'''
<h1 style='color:blue>Meu curso é; </h1>
<p>GTI <b>OI</b>
'''

@app.route('/var')
def variavel():
    palavra = 'Vinicius'
    return f'<h1>Adicionando texto de var: {palavra}'

@app.route('/idade/Int:ano')
def idade(ano):
    calculoIdade = 2026 - ano
    return f'Voce tem {calculoIdade} anos'

@app.route('/salvar/<nome>/produtos')
def salvar(nome):
    return f'Você salvou o produto[{nome}] com sucesso!'

@app.route('/html')
def pagina_html():
    return render_template('index.html')

@app.route('/calcular/<nome>/<int:ano>')
def calcular(nome, ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade > 18:
        status = 'Maior de idade'
    else:
        status = 'Menor de idade - ACESSO NEGADO!'

    return render_template('variaveis.html', nome_usuario = nome, ano_atual = ano_atual, nascimento = ano, idade = idade, status = status)































#---ULTIMA COISA DO ARQUIVO
if __name__ == '__main__':
    app.run(debug=True)