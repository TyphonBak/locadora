import factory
from app.BLL.models.cliente import Cliente
from app.BLL.models.filme import Filme
from app.extensions import db

class ClienteFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Cliente
        sqlalchemy_session = db.session

    nome = factory.Faker('name', locale='pt_BR')
    email = factory.Faker('email', locale='pt_BR')
    telefone = factory.Faker('numerify', text='###########')

class FilmeFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Filme
        sqlalchemy_session = db.session

    titulo = factory.Faker('name')
    ano = factory.Faker('year')
    genero = factory.Faker('word')
    preco = factory.Faker('pyfloat', positive=True, right_digits=2)
    estoque = factory.Faker('pyint', min_value=0, max_value=100)
    sinopse = factory.Faker('paragraph', nb_sentences=1)
    classificacao = factory.Faker('word')
    diretor = factory.Faker('name')
