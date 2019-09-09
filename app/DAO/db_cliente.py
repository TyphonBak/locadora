from app.extensions import db
from app.BLL.models.cliente import Cliente

def lista():
    clientes = Cliente.query.all()
    [cli.__dict__.pop('_sa_instance_state') for cli in clientes]
    return clientes

def busca(id):
    cliente = Cliente.query.get(id)
    if cliente:
        cliente.__dict__.pop('_sa_instance_state')
    return cliente

def adiciona(cliente):
    try:
        db.session.add(cliente)
        db.session.commit()

        novo = Cliente.query.order_by(Cliente.id.desc()).first()
        novo.__dict__.pop('_sa_instance_state')
        return novo.__dict__
    except Exception as error:
        db.session.rollback()    
        return str(error.orig)

def altera(id, dados):
    try:
        Cliente.query.filter_by(id=id).update(dados)
        db.session.commit()
        cliente = busca(id)

        return cliente
    except TypeError as error:
        return str(error)
    except Exception as error:
        return str(error.orig)

def deleta(id):
    try:
        cliente = Cliente.query.get(id)
        if cliente == None:
            return None
        db.session.delete(cliente)
        db.session.commit()
        return 'No Content'
    except Exception as error:
        return str(error)

