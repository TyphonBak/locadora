from app.BLL.models.filme import Filme
from app.DAO.db_filme import lista as lista_db, adiciona as adiciona_db, busca as busca_db, altera as altera_db, deleta as deleta_db

def lista():
    filmes = lista_db()

    conteudo = [film.__dict__ for film in filmes]
    return {'conteudo': conteudo, 'code': 200}

def busca(id):
    result = busca_db(id)
    if isinstance(result, Filme):
        conteudo, code = result.__dict__, 200
    else:
        conteudo, code = result, 404
    return {'conteudo': conteudo, 'code': code}

def adiciona(dados):
    filme = Filme.cria(dados)
    result = adiciona_db(filme)
    if not isinstance(result, dict):
        result, code = {'errors': result}, 400
    else:
        code = 201
    return {'conteudo': result, 'code': code}

def altera(id, dados):
    result = altera_db(id, dados)
    if isinstance(result, Filme):
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
