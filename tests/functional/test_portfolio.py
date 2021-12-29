from main import create_app

def test_read_portfolio():
  flask_app = create_app()
  with flask_app.test_client() as client:
    response = client.get('/api/portfolios/1')
    assert response.status_code == 200

def test_update_portfolio():
  flask_app = create_app()
  with flask_app.test_client() as client:
    response = client.put('/api/portfolios/1', json={'email': 'example@example.com', 'name': 'aaaaaa'})
    assert response.status_code == 200