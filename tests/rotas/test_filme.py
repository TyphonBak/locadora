from pytest import set_trace
from flask import url_for
from tests.helper import client, test_app, db
from tests.models_factory import FilmeFactory

# GET SESSION
def test_get_deve_retornar_lista_de_filmes(client, db):
    result = client.get(url_for('Filme BP.lista'))
    assert result.status_code == 200
    assert type(result.json) == list

def test_get_deve_retornar_404_quando_nao_houver_id(client, db):
    result = client.get(url_for('Filme BP.busca', id=9999))
    assert result.status_code == 404

# POST SESSION
def test_post_deve_retornar_201_e_filme_criado(client, db):
    filme = FilmeFactory.build()
    filme.__dict__.pop('_sa_instance_state')

    result = client.post(url_for('Filme BP.adiciona'), json=filme.__dict__)

    assert result.status_code == 201
    assert all(elem in result.json.keys() for elem in filme.__dict__.keys())
    assert 'id' in result.json
    

def test_post_deve_retornar_400_quando_informacoes_erradas_forem_enviadas(client, db):
    filme = FilmeFactory.build()
    filme.titulo = None
    filme.__dict__.pop('_sa_instance_state')

    result = client.post(url_for('Filme BP.adiciona'), json=filme.__dict__)

    assert result.status_code == 400
    assert 'errors' in result.json

## WITH ID SESSION

#GET
def test_get_deve_retornar_200_e_filme_quando_id_existir(client, db):
    filme = FilmeFactory.build()
    filme.__dict__.pop('_sa_instance_state')

    client.post(url_for('Filme BP.adiciona'), json=filme.__dict__)
    result = client.get(url_for('Filme BP.busca', id=1))

    assert result.status_code == 200
    assert all(elem in result.json.keys() for elem in filme.__dict__.keys())

#PUT
def test_put_deve_retornar_200_e_filme_alterado(client, db):
    filme = FilmeFactory.build()
    filme.__dict__.pop('_sa_instance_state')

    filme_criado = client.post(url_for('Filme BP.adiciona'), json=filme.__dict__).json

    filme_criado['titulo'] = 'Novo titulo'

    result = client.put(url_for('Filme BP.altera', id=filme_criado.get('id')), json=filme_criado)

    assert result.status_code == 200
    assert result.json['id'] == filme_criado['id']
    assert result.json['titulo'] == filme_criado['titulo']

def test_put_deve_retornar_404_quando_id_nao_existir(client, db):
    filme = FilmeFactory.build()
    filme.__dict__.pop('_sa_instance_state')

    result = client.put(url_for('Filme BP.altera', id=99), json=filme.__dict__)

    assert result.status_code == 404
    assert result.json == None

def test_put_deve_retornar_400_quando_nao_for_passado_dados(client, db):
    filme = FilmeFactory.build()
    filme.__dict__.pop('_sa_instance_state')

    filme_criado = client.post(url_for('Filme BP.adiciona'), json=filme.__dict__).json
    result = client.put(url_for('Filme BP.altera', id=filme_criado.get('id')), json={})

    assert result.status_code == 400

#DELETE
def test_delete_deve_retornar_404_quando_id_nao_existir(client, db):
    result = client.delete(url_for('Filme BP.deleta', id=999))

    assert result.json == None
    assert result.status_code == 404

def test_delete_deve_permitir_delecao_de_filme_existente(client, db):
    filme = FilmeFactory.build()
    filme.__dict__.pop('_sa_instance_state')

    filme_criado = client.post(url_for('Filme BP.adiciona'), json=filme.__dict__).json
    result = client.delete(url_for('Filme BP.deleta', id=filme_criado.get("id")))

    assert result.status_code == 204