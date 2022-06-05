class TestIndex:
    def test_get(self, client):
        response = client.get('/')
        assert 200 == response.status_code
