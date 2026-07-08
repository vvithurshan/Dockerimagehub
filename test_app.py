from app import app

# Need to start with test
def test_home():
    response = app.test_client("/")

    assert response.status_code == 200
    assert response.data == b"<h1>Hello World</h1>"
