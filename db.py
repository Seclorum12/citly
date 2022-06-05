from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class DB(SQLAlchemy):
    def __init__(self, app: Flask):
        super().__init__(app)
        self._app = app

    def create_all(self, bind: str = '__all__', app: Flask = None) -> None:
        from modules.links.models import Link  # noqa
        return super().create_all(bind, app)
