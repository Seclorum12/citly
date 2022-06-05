from modules.links.factories import LinkFactory


class TestIndex:
    def test_get(self, client):
        response = client.get('/')
        assert 200 == response.status_code


class TestFollow:
    def test_non_existed(self, client):
        response = client.get('/fake_link')
        assert 404 == response.status_code

    def test_existed(self, client, db):
        link_in_db = LinkFactory.create()
        db.session.commit()
        response = client.get(f'/{link_in_db.generated_link}')
        assert 302 == response.status_code
