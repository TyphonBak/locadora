from app.extensions import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)

    @staticmethod
    def cria(dados):
        try:
            nome = dados['nome']
            email = dados['email']
            telefone = dados['telefone']
            return Cliente(nome=nome, email=email, telefone=telefone)
        except Exception as e:
            return e

    @staticmethod
    def cria_de_tupla(dados):
        try:
            print(dados)
            nome = dados[0]
            email = dados[1]
            telefone = dados[3]
            return Cliente(nome=nome, email=email, telefone=telefone)
        except Exception as e:
            return e
