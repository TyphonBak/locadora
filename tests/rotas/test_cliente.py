from pytest import set_trace
from flask import url_for
from tests.helper import client, test_app, db
from tests.models_factory import ClienteFactory

# GET SESSION
def test_get_deve_retornar_lista_de_clientes(client, db):
    result = client.get(url_for('Cliente BP.lista'))
    assert result.status_code == 200
    assert type(result.json) == list

def test_get_deve_retornar_404_quando_nao_houver_id(client, db):
    result = client.get(url_for('Cliente BP.busca', id=999))
    assert result.status_code == 404

# POST SESSION
def test_post_deve_retornar_201_e_cliente_criado(client, db):
    cliente = ClienteFactory.build()
    cliente.__dict__.pop('_sa_instance_state')

    result = client.post(url_for('Cliente BP.adiciona'), json=cliente.__dict__)

    assert result.status_code == 201
    assert all(elem in result.json.keys() for elem in cliente.__dict__.keys())
    assert 'id' in result.json
    

def test_post_deve_retornar_400_quando_informacoes_erradas_forem_enviadas(client, db):
    cliente = ClienteFactory.build()
    cliente.nome = None
    cliente.__dict__.pop('_sa_instance_state')

    result = client.post(url_for('Cliente BP.adiciona'), json=cliente.__dict__)

    assert result.status_code == 400
    assert 'errors' in result.json

## WITH ID SESSION

#GET
def test_get_deve_retornar_200_e_cliente_quando_id_existir(client, db):
    cliente = ClienteFactory.build()
    cliente.__dict__.pop('_sa_instance_state')

    client.post(url_for('Cliente BP.adiciona'), json=cliente.__dict__)
    result = client.get(url_for('Cliente BP.busca', id=1))

    assert result.status_code == 200
    assert all(elem in result.json.keys() for elem in cliente.__dict__.keys())

#PUT
def test_put_deve_retornar_200_e_cliente_alterado(client, db):
    cliente = ClienteFactory.build()
    cliente.__dict__.pop('_sa_instance_state')

    cliente_criado = client.post(url_for('Cliente BP.adiciona'), json=cliente.__dict__).json

    cliente_criado['nome'] = 'Novo Nome'

    result = client.put(url_for('Cliente BP.altera', id=cliente_criado.get("id")), json=cliente_criado)

    assert result.status_code == 200
    assert result.json['id'] == cliente_criado['id']
    assert result.json['nome'] == cliente_criado['nome']

def test_put_deve_retornar_404_quando_id_nao_existir(client, db):
    cliente = ClienteFactory.build()
    cliente.__dict__.pop('_sa_instance_state')

    result = client.put(url_for('Cliente BP.altera', id=99), json=cliente.__dict__)

    assert result.status_code == 404
    assert result.json == None

def test_put_deve_retornar_400_quando_nao_for_passado_dados(client, db):
    cliente = ClienteFactory.build()
    cliente.__dict__.pop('_sa_instance_state')

    cliente_criado = client.post(url_for('Cliente BP.adiciona'), json=cliente.__dict__).json
    result = client.put(url_for('Cliente BP.altera', id=cliente_criado.get("id")), json={})

    assert result.status_code == 400

#DELETE
def test_delete_deve_retornar_404_quando_id_nao_existir(client, db):
    result = client.delete(url_for('Cliente BP.deleta', id=999))

    assert result.json == None
    assert result.status_code == 404

def test_delete_deve_permitir_delecao_de_cliente_existente(client, db):
    cliente = ClienteFactory.build()
    cliente.__dict__.pop('_sa_instance_state')

    cliente_criado = client.post(url_for('Cliente BP.adiciona'), json=cliente.__dict__).json
    result = client.delete(url_for('Cliente BP.deleta', id=cliente_criado.get("id")))

    assert result.status_code == 204
