from flask import Flask, jsonify, request
import time
import os
from datetime import datetime

app = Flask(__name__)

# Lista zadań
todos = [
    {"id": 1, "title": "Stworzenie aplikacji Flask", "completed": True},
    {"id": 2, "title": "Dodanie testów", "completed": False},
    {"id": 3, "title": "Konfiguracja CI/CD", "completed": False}
]

@app.route('/')
def home():
    """Endpoint główny"""
    return jsonify({
        "message": "Projekt zaliczeniowy - Lab 1-3 (Python Flask)",
        "author": "Klaudia Derlatka",
        "version": "1.0.0",
        "description": "Aplikacja demonstrujaca umiejetnosci Git/GitHub, workflow i CI/CD"
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "OK",
        "timestamp": datetime.utcnow().isoformat(),
        "uptime": time.time(),
        "version": "1.0.0"
    })

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """Pobierz wszystkie zadania"""
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def create_todo():
    """Utwórz nowe zadanie"""
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_todo = {
        "id": len(todos) + 1,
        "title": data['title'],
        "completed": False
    }
    
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/about')
def about():
    """Informacje o projekcie"""
    return jsonify({
        "project": "Lab Projekt Zaliczenie - Flask",
        "technologies": ["Python", "Flask", "pytest", "Docker", "GitHub Actions"],
        "features": [
            "Git workflow z gałęziami i PR",
            "Automatyczne testy",
            "CI/CD pipeline",
            "Containerization",
            "Deployment w chmurze"
        ],
        "lab_topics": [
            "Lab 1: Podstawy Git/GitHub",
            "Lab 2: Zaawansowany Git workflow",
            "Lab 3: CI/CD i deployment"
        ]
    })

@app.route('/api/status')
def api_status():
    """Status API endpoint"""
    return jsonify({
        "api_status": "running",
        "environment": os.environ.get('FLASK_ENV', 'development'),
        "timestamp": datetime.utcnow().isoformat()
    })


@app.errorhandler(404)
def not_found(error):
    """Handler dla 404"""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handler dla błędów serwera"""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 