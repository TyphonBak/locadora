from app.extensions import db
from app.BLL.models.filme import Filme

def lista():
    filmes = Filme.query.all()
    [film.__dict__.pop('_sa_instance_state') for film in filmes]
    return filmes

def busca(id):
    filme = Filme.query.get(id)
    if filme:
        filme.__dict__.pop('_sa_instance_state')
    return filme

def adiciona(filme):
    try:
        db.session.add(filme)
        db.session.commit()

        novo = Filme.query.order_by(Filme.id.desc()).first()
        novo.__dict__.pop('_sa_instance_state')
        return novo.__dict__
    except Exception as error:
        db.session.rollback()    
        return str(error.orig)

def altera(id, dados):
    try:
        Filme.query.filter_by(id=id).update(dados)
        db.session.commit()
        filme = busca(id)

        return filme
    except TypeError as error:
        return str(error)
    except Exception as error:
        return str(error.orig)

def deleta(id):
    try:
        filme = Filme.query.get(id)
        if filme == None:
            return None
        db.session.delete(filme)
        db.session.commit()
        return 'No Content'
    except Exception as error:
        return str(error)

