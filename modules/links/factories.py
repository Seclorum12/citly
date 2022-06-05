import factory

from app import db
from modules.links.models import Link


class LinkFactory(factory.alchemy.SQLAlchemyModelFactory):
    original_link = factory.Faker('url')
    generated_link = factory.Faker('nic_handle')
    follows = 10

    class Meta:
        model = Link
        sqlalchemy_session = db.session
