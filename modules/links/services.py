import secrets

from app import db
from modules.links.models import Link


class LinksService:

    def get_or_generate_short_link(self, original_link: str) -> tuple[Link, bool]:
        """
        :param original_link:
        :return: Short link and True if generated new one, False if link from DB
        """
        db_original_link = Link.query.filter_by(original_link=original_link).first()
        if db_original_link:
            return db_original_link, False

        link = Link(original_link=original_link, generated_link=self.create_random_link())
        db.session.add(link)
        db.session.commit()
        return link, True

    def create_random_link(self, _attempts=0):
        max_attempts = 20
        token = secrets.token_urlsafe(12)
        link = Link.query.filter_by(generated_link=token).first()
        if _attempts >= max_attempts:
            raise RecursionError(f'Maximum attempts ({max_attempts}) exceeded.')
        if link:
            _attempts += 1
            self.create_random_link(_attempts=_attempts)
        return token
