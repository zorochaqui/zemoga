from main import create_app

def test_tweet():
  flask_app = create_app()
  with flask_app.test_client() as client:
    response = client.get('/api/portfolios/name/Zemoga/tweets/10')
    assert response.status_code == 200