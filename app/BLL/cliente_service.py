from app.BLL.models.cliente import Cliente
from app.DAO.db_cliente import lista as lista_db, adiciona as adiciona_db, busca as busca_db, altera as altera_db, deleta as deleta_db

def lista():
    clientes = lista_db()

    conteudo = [cli.__dict__ for cli in clientes]
    return {'conteudo': conteudo, 'code': 200}

def busca(id):
    result = busca_db(id)
    if isinstance(result, Cliente):
        conteudo, code = result.__dict__, 200
    else:
        conteudo, code = result, 404
    return {'conteudo': conteudo, 'code': code}

def adiciona(dados):
    cliente = Cliente.cria(dados)
    result = adiciona_db(cliente)
    if not isinstance(result, dict):
        result, code = {'errors': result}, 400
    else:
        code = 201
    return {'conteudo': result, 'code': code}

def altera(id, dados):
    result = altera_db(id, dados)
    if isinstance(result, Cliente):
        result, code = result.__dict__, 200
    elif result == None:
        code = 404
    else:
        code = 400
    return {'conteudo': result, 'code': code}

def deleta(id):
    result = deleta_db(id)
    if result == None:
        code = 404
    elif result == 'No Content':
        code = 204
    else:
        code = 400
    return {'conteudo': result, 'code': code}
