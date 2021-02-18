

def test_valid_request(app, client):
    '''Echo request to validate server processing correctly.'''

    response = client.get('/', headers={'User-Agent': 'Test-Header'})

    assert response.status_code == 200
    assert response.json.get('user-agent') == 'Test-Header'


def test_404_request(app, client):
    '''Echo request for a non-existent address.'''

    response = client.get('/something-that-cannot-be-exist')

    assert response.status_code == 404
