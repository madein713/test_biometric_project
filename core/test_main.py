def test_auth(db, client):
    response = client.post('/auth/', {'username': 'testusername', 'password': 'testpassword'})
    assert response.status_code == 200
    data = response.json()
    assert 'token' in data
    assert 'user_id' in data
