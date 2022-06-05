import os

import pytest

os.environ['FLASK_ENV'] = 'testing'


@pytest.fixture()
def app():
    from app import app
    yield app


@pytest.fixture()
def db(app):
    from app import db
    db.init_app(app)
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture()
def client(app, db):
    """
    :param app: Flask app
    :param db: DB used for tests. Used for DB clean up
    :return: Test client
    """
    yield app.test_client()
