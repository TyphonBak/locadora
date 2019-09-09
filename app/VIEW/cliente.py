from flask import Blueprint, jsonify, request
from app.BLL.cliente_service import lista as lista_service, busca as busca_service, adiciona as adiciona_service, altera as altera_service, deleta as deleta_service

bp_cliente = Blueprint('Cliente BP', __name__)

@bp_cliente.route('/api/clientes')
def lista():
    result = lista_service()
    return jsonify(result.get('conteudo')), result.get('code')

@bp_cliente.route('/api/clientes/<int:id>')
def busca(id):
    result = busca_service(id)
    return jsonify(result.get('conteudo')), result.get('code')

@bp_cliente.route('/api/clientes', methods=['POST'])
def adiciona():
    result = adiciona_service(request.get_json())
    return jsonify(result.get('conteudo')), result.get('code')

@bp_cliente.route('/api/clientes/<int:id>', methods=['PUT'])
def altera(id):
    result = altera_service(id, request.get_json())
    return jsonify(result['conteudo']), result['code']

@bp_cliente.route('/api/clientes/<int:id>', methods=['DELETE'])
def deleta(id):
    result = deleta_service(id)
    return jsonify(result['conteudo']), result['code']