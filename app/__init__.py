from flask import Flask
from .extensions import db

from app.VIEW.cliente import bp_cliente
from app.VIEW.filme import bp_filme
from app.VIEW.web import bp_web

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    app.register_blueprint(bp_cliente)
    app.register_blueprint(bp_filme)
    app.register_blueprint(bp_web)

    db.init_app(app)

    return app
