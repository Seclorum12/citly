class TestMakeShortLink:
    def test_post(self, client):
        response = client.post('api/links/make-short-link', json={'link': 'https://github.com'})
        assert response.status_code == 200

    def test_post_empty_data(self, client):
        response = client.post('api/links/make-short-link', json={})
        assert response.status_code == 400

    def test_post_wrong_key(self, client):
        response = client.post('api/links/make-short-link', json={'wrong_key': 'https://github.com'})
        assert response.status_code == 400

    def test_post_wrong_url(self, client):
        response = client.post('api/links/make-short-link', json={'link': 'this-is-not-url'})
        assert response.status_code == 400

    def test_post_own_url(self, client):
        response = client.post('api/links/make-short-link', json={'link': 'http://localhost/'})
        assert response.status_code == 400
