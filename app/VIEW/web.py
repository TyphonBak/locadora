from flask import Blueprint, render_template, url_for
from app.VIEW.filme import lista as lista_filmes
from app.VIEW.cliente import lista as lista_clientes

bp_web = Blueprint('Web BP', __name__)

@bp_web.route('/')
def index():
    return render_template('index.html')

@bp_web.route('/filmes')
def filmes():
    lista_de_filmes = lista_filmes()[0].json
    context = {'filmes': lista_de_filmes}
    return render_template('filmes.html', context=context)

@bp_web.route('/clientes')
def clientes():
    lista_de_clientes = lista_clientes()[0].json
    context = {'clientes': lista_de_clientes}
    return render_template('clientes.html', context=context)
