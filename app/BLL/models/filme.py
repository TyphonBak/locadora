from app.extensions import db

class Filme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    sinopse = db.Column(db.Text, unique=True, nullable=False)
    classificacao = db.Column(db.String(5), nullable=False)
    diretor = db.Column(db.String(50), nullable=False)

    @staticmethod
    def cria(dados):
        try:
            titulo = dados['titulo']
            ano = dados['ano']
            genero = dados['genero']
            preco = dados['preco']
            estoque = dados['estoque']
            sinopse = dados['sinopse']
            classificacao = dados['classificacao']
            diretor = dados['diretor']
            return Filme(titulo=titulo, ano=ano, genero=genero, preco=preco, estoque=estoque, sinopse=sinopse, classificacao=classificacao, diretor=diretor)
        except Exception as e:
            return e

    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            titulo = dados[1]
            ano = dados[2]
            genero = dados[3]
            preco = dados[4]
            estoque = dados[5]
            sinopse = dados[6]
            classificacao = dados[7]
            diretor = dados[8]
            return Filme(id=id, titulo=titulo, ano=ano, genero=genero, preco=preco, estoque=estoque, sinopse=sinopse, classificacao=classificacao, diretor=diretor)
        except Exception as e:
            return e
