import pytest
import json
from app import app

@pytest.fixture
def client():
    """Konfiguracja klienta testowego Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestFlaskApp:
    """Testy aplikacji Flask"""
    
    def test_home_endpoint(self, client):
        """Test endpointu głównego"""
        response = client.get('/')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'message' in data
        assert 'author' in data
        assert 'version' in data
        assert data['version'] == '1.0.0'
        assert 'Python Flask' in data['message']
    
    def test_health_endpoint(self, client):
        """Test health check"""
        response = client.get('/health')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['status'] == 'OK'
        assert 'timestamp' in data
        assert 'uptime' in data
        assert 'version' in data
    
    def test_get_todos(self, client):
        """Test pobierania zadań"""
        response = client.get('/api/todos')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) > 0
        
        # Sprawdź strukturę pierwszego zadania
        first_todo = data[0]
        assert 'id' in first_todo
        assert 'title' in first_todo
        assert 'completed' in first_todo
    
    def test_create_todo_success(self, client):
        """Test tworzenia nowego zadania"""
        new_todo = {"title": "Test zadanie"}
        
        response = client.post('/api/todos',
                              data=json.dumps(new_todo),
                              content_type='application/json')
        
        assert response.status_code == 201
        data = json.loads(response.data)
        assert 'id' in data
        assert data['title'] == 'Test zadanie'
        assert data['completed'] == False
    
    def test_create_todo_missing_title(self, client):
        """Test tworzenia zadania bez tytułu"""
        response = client.post('/api/todos',
                              data=json.dumps({}),
                              content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
        assert data['error'] == 'Title is required'
    
    def test_about_endpoint(self, client):
        """Test endpointu about"""
        response = client.get('/about')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'project' in data
        assert 'technologies' in data
        assert 'features' in data
        assert 'lab_topics' in data
        
        assert isinstance(data['technologies'], list)
        assert 'Python' in data['technologies']
        assert 'Flask' in data['technologies']
    
    def test_api_status_endpoint(self, client):
        """Test endpointu API status"""
        response = client.get('/api/status')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'api_status' in data
        assert data['api_status'] == 'running'
    
    def test_api_metrics_endpoint(self, client):
        """Test endpointu metrics"""
        response = client.get('/api/metrics')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'requests_count' in data
        assert 'uptime_seconds' in data
    
    def test_404_handler(self, client):
        """Test handlera 404"""
        response = client.get('/nieistniejacy-endpoint')
        assert response.status_code == 404
        
        data = json.loads(response.data)
        assert 'error' in data
        assert data['error'] == 'Endpoint not found' 