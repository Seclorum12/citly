import pytest
import secrets
from modules.links.factories import LinkFactory
from modules.links.services import LinksService


@pytest.fixture()
def service(db):
    return LinksService()


class TestGetOrGenerateShortUrl:
    def test_get_existed_link(self, db, service):
        link = LinkFactory()
        db.session.commit()
        retrieved_link, is_created = service.get_or_generate_short_link(original_link=link.original_link)
        assert not is_created
        assert link.id == retrieved_link.id

    def test_generate_new_one(self, db, service):
        original_link = 'https://github.com'
        link, is_created = service.get_or_generate_short_link(original_link=original_link)
        assert is_created
        assert link.id
        assert original_link == link.original_link
        assert link.generated_link


class TestCreateRandomLink:
    def test_creation(self, service):
        assert service.create_random_link()

    def test_recursion(self, db, service, mocker):
        fake_random_link = 'not_random'
        LinkFactory(generated_link=fake_random_link)
        db.session.commit()
        mocked_token_urlsafe = mocker.patch.object(secrets, 'token_urlsafe', return_value=fake_random_link)
        with pytest.raises(RecursionError):
            service.create_random_link()

        assert mocked_token_urlsafe.call_count == 21
