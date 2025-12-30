import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'message' in data

def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_hello_endpoint_default(client):
    """Test hello endpoint with default name"""
    response = client.get('/api/hello')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Hello, World!'
    assert data['status'] == 'success'

def test_hello_endpoint_with_name(client):
    """Test hello endpoint with custom name"""
    response = client.get('/api/hello?name=Jenkins')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Hello, Jenkins!'
    assert data['status'] == 'success'

def test_add_endpoint_success(client):
    """Test add endpoint with valid numbers"""
    response = client.post('/api/add', 
                          json={'a': 5, 'b': 3},
                          content_type='application/json')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 8
    assert data['status'] == 'success'

def test_add_endpoint_missing_params(client):
    """Test add endpoint with missing parameters"""
    response = client.post('/api/add', 
                          json={'a': 5},
                          content_type='application/json')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_add_endpoint_no_json(client):
    """Test add endpoint with no JSON data"""
    response = client.post('/api/add')
    assert response.status_code == 415
    data = response.get_json()
    assert 'error' in data

def test_add_endpoint_invalid_numbers(client):
    """Test add endpoint with invalid number format"""
    response = client.post('/api/add', 
                          json={'a': 'invalid', 'b': 3},
                          content_type='application/json')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

