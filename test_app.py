from app import app

# Need to start with test
def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"<h1>Hello World</h1>"