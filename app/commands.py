import click
from flask.cli import with_appcontext

from app.extensions import db
from app.BLL.models.cliente import Cliente
from app.BLL.models.filme import Filme

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()