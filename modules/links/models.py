from app import db
from utils.db import BaseModel


class Link(BaseModel):
    __tablename__ = 'links_link'

    original_link = db.Column(db.String(2084), nullable=False, unique=True)
    generated_link = db.Column(db.String(256), nullable=False, unique=True)
    follows = db.Column(db.Integer, default=0, nullable=False)
