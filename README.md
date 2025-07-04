# Lab Projekt Zaliczenie - Python Flask

![CI/CD Status](https://github.com/USERNAME/REPOSITORY/workflows/Python%20Flask%20CI/CD/badge.svg)

Projekt zaliczeniowy demonstrujący umiejętności z laboratoriów 1-3: Git/GitHub, zaawansowany workflow oraz CI/CD w **Python Flask**.

## 📋 Spis treści

- [Opis projektu](#opis-projektu)
- [Technologie](#technologie)
- [Funkcjonalności](#funkcjonalności)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [API Endpoints](#api-endpoints)
- [Testowanie](#testowanie)
- [Docker](#docker)
- [CI/CD Pipeline](#cicd-pipeline)
- [Deployment](#deployment)
- [Laboratorium](#laboratorium)

## 🎯 Opis projektu

Prosta aplikacja webowa w **Python Flask**, która demonstruje:

- **Lab 1**: Podstawy Git/GitHub - tworzenie repozytorium, commits, dokumentacja
- **Lab 2**: Zaawansowany Git workflow - gałęzie, pull requesty, rozwiązywanie konfliktów
- **Lab 3**: CI/CD i deployment w chmurze - automatyzacja, testy, wdrażanie

Aplikacja udostępnia REST API do zarządzania zadaniami (todos) oraz informacje o projekcie.

## 🛠️ Technologie

- **Backend**: Python 3.11, Flask
- **Testy**: pytest, pytest-flask
- **Konteneryzacja**: Docker, Gunicorn
- **CI/CD**: GitHub Actions
- **Deployment**: Heroku / AWS / Azure
- **Dokumentacja**: Markdown

## ✨ Funkcjonalności

- ✅ REST API do zarządzania zadaniami
- ✅ Health check endpoint
- ✅ Informacje o projekcie i użytych technologiach
- ✅ Obsługa błędów 404 i 500
- ✅ Automatyczne testy z pytest
- ✅ Docker containerization z Gunicorn
- ✅ CI/CD pipeline z GitHub Actions
- ✅ Automatyczny deployment

## 🚀 Instalacja

### Lokalnie

```bash
# Klonowanie repozytorium
git clone https://github.com/USERNAME/lab-projekt-zaliczenie-flask.git

# Przejście do katalogu projektu
cd lab-projekt-zaliczenie-flask

# Utworzenie środowiska wirtualnego
python -m venv venv

# Aktywacja środowiska (Windows)
venv\Scripts\activate
# Aktywacja środowiska (Linux/Mac)
source venv/bin/activate

# Instalacja zależności
pip install -r requirements.txt

# Uruchomienie aplikacji
python app.py
```

### Docker

```bash
# Budowanie obrazu Docker
docker build -t flask-projekt .

# Uruchomienie kontenera
docker run -p 5000:5000 flask-projekt
```

## 💻 Użycie

Po uruchomieniu aplikacja będzie dostępna pod adresem: `http://localhost:5000`

### Główne endpointy:

- `GET /` - Informacje o projekcie
- `GET /health` - Status zdrowia aplikacji
- `GET /about` - Szczegółowe informacje o technologiach
- `GET /api/todos` - Lista zadań
- `POST /api/todos` - Utworzenie nowego zadania

## 📚 API Endpoints

### GET /
```json
{
  "message": "Projekt zaliczeniowy - Lab 1-3 (Python Flask)",
  "author": "Twoje Imię",
  "version": "1.0.0",
  "description": "Aplikacja demonstrująca umiejętności Git/GitHub, workflow i CI/CD"
}
```

### GET /health
```json
{
  "status": "OK",
  "timestamp": "2024-01-01T00:00:00.000000",
  "uptime": 3600.0,
  "version": "1.0.0"
}
```

### GET /api/todos
```json
[
  {
    "id": 1,
    "title": "Stworzenie aplikacji Flask",
    "completed": true
  }
]
```

### POST /api/todos
```bash
curl -X POST http://localhost:5000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Nowe zadanie"}'
```

## 🧪 Testowanie

```bash
# Uruchomienie testów
pytest

# Testy z szczegółowym outputem
pytest -v

# Pokrycie kodu testami
pip install pytest-cov
pytest --cov=app --cov-report=html
```

Testy obejmują:
- Testy jednostkowe wszystkich endpointów
- Testy integracyjne API Flask
- Walidację JSON responses
- Obsługę błędów HTTP

## 🐳 Docker

### Budowanie obrazu
```bash
docker build -t flask-projekt .
```

### Uruchomienie
```bash
docker run -p 5000:5000 flask-projekt
```

### Testowanie kontenera
```bash
# Sprawdzenie health check
curl http://localhost:5000/health
```

## 🔄 CI/CD Pipeline

Pipeline GitHub Actions wykonuje:

1. **Test**: 
   - Testowanie na Python 3.9, 3.10, 3.11
   - Uruchomienie testów pytest
   - Generowanie raportu pokrycia

2. **Docker Build**:
   - Budowanie obrazu Docker
   - Testowanie kontenera z Gunicorn

3. **Deploy**:
   - Automatyczne wdrożenie na main branch
   - Health check po deployment

## 🚀 Deployment

### Heroku
```bash
# Instalacja Heroku CLI i login
heroku create nazwa-aplikacji

# Dodanie Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
git add Procfile
git commit -m "feat: add Procfile for Heroku"
git push heroku main
```

### AWS/Azure
Szczegóły konfiguracji w `.github/workflows/python-ci-cd.yml`

## 🎓 Laboratorium

### Lab 1: Podstawy Git/GitHub ✅
- [x] Utworzenie repozytorium
- [x] Podstawowe commits
- [x] Dokumentacja README.md
- [x] Konfiguracja .gitignore

### Lab 2: Zaawansowany Git workflow ✅
- [x] Praca z gałęziami (feature branches)
- [x] Pull requesty i code review
- [x] Rozwiązywanie konfliktów merge
- [x] Tagowanie wersji (semantic versioning)
- [x] Testy automatyczne z pytest

### Lab 3: CI/CD i deployment ✅
- [x] GitHub Actions pipeline
- [x] Docker konteneryzacja z Gunicorn
- [x] Automatyczne testy w CI
- [x] Deployment w chmurze
- [x] Health checks i monitoring

## 📝 Workflow Git

Projekt wykorzystuje:
- **Main branch** - wersja produkcyjna
- **Develop branch** - wersja deweloperska
- **Feature branches** - nowe funkcjonalności
- **Pull requests** - code review
- **Semantic versioning** - tagowanie wersji

## 🤝 Contributing

1. Fork repozytorium
2. Utwórz feature branch (`git checkout -b feature/nowa-funkcjonalnosc`)
3. Commit zmian (`git commit -m 'feat: dodanie nowej funkcjonalności'`)
4. Push do branch (`git push origin feature/nowa-funkcjonalnosc`)
5. Utwórz Pull Request

## 📄 Licencja

Projekt jest licencjonowany pod [licencją MIT](LICENSE).

## 👨‍💻 Autor

**Twoje Imię** - Projekt zaliczeniowy  
GitHub: [@USERNAME](https://github.com/USERNAME)

## 🙏 Podziękowania

- Materiały z laboratoriów 1-3
- Dokumentacja Flask, pytest, Docker
- GitHub Actions Community 