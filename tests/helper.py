import pytest
from app.extensions import db as _db
from app import create_app

@pytest.fixture
def test_app():
    _app = create_app()
    _app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    _app.config['TESTING'] = True
    _app.config['USE_RELOADER'] = False
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

@pytest.fixture
def db(test_app):
    _db.app = test_app
    with test_app.app_context():
        _db.drop_all()
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()

@pytest.fixture
def client(test_app):

    client = test_app.test_client()

    return client

