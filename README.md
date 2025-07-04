# 💻 Lab Projekt Zaliczeniowy – Python Flask

Projekt końcowy obejmujący zakres laboratoriów 1–3 z przedmiotu: Git/GitHub, workflow developerski oraz CI/CD na przykładzie aplikacji webowej opartej o **Python Flask**.

---

## 📁 Spis treści

* [Opis](#opis)
* [Technologie](#technologie)
* [Funkcje](#funkcje)
* [Instalacja](#instalacja)
* [Użycie](#u017cycie)
* [API](#api)
* [Testowanie](#testowanie)
* [Docker](#docker)
* [CI/CD](#cicd)
* [Deployment](#deployment)
* [Laboratoria](#laboratoria)
* [Workflow Git](#workflow-git)
* [Contributing](#contributing)
* [Licencja](#licencja)
* [Autor](#autor)

---

## 📌 Opis

Aplikacja webowa w **Python Flask**, której celem jest demonstracja praktycznych umiejętności z laboratoriów:

* **Lab 1**: Praca z Git/GitHub – repozytorium, commity, pliki konfiguracyjne
* **Lab 2**: Zaawansowany workflow – branchowanie, pull requesty, rozwiązywanie konfliktów
* **Lab 3**: CI/CD – testowanie, automatyzacja i wdrożenie na środowisko zewnętrzne

Aplikacja udostępnia REST API do zarządzania zadaniami (todos) i zawiera podstawowe informacje o systemie.

---

## ⚙️ Technologie

* **Język backendowy**: Python 3.11 + Flask
* **Testy**: pytest, pytest-flask
* **Konteneryzacja**: Docker, Gunicorn
* **CI/CD**: GitHub Actions
* **Deployment**: Heroku / AWS / Azure
* **Dokumentacja**: Markdown

---

## ✅ Funkcje

* REST API dla CRUD zadań
* Endpoint `health check`
* Informacje o technologii i wersji aplikacji
* Obsługa błędów HTTP 404 i 500
* Automatyczne testy jednostkowe i integracyjne
* Konteneryzacja Docker + Gunicorn
* Pipeline CI/CD z testami i deploymentem

---

## 🧹 Instalacja

### Wersja lokalna

```bash
git clone https://github.com/Dusiaxk/lab-projekt-zaliczenie-flask.git
cd lab-projekt-zaliczenie-flask

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

### Wersja Docker

```bash
docker build -t flask-projekt .
docker run -p 5000:5000 flask-projekt
```

---

## 💻 Użycie

Aplikacja uruchamia się domyślnie pod adresem:
`http://localhost:5000`

### Endpointy:

* `GET /` – informacje o projekcie
* `GET /health` – stan aplikacji
* `GET /about` – szczegóły techniczne
* `GET /api/todos` – lista zadań
* `POST /api/todos` – dodanie zadania

---

## 🔌 API

### `GET /`

```json
{
  "message": "Projekt zaliczeniowy - Lab 1-3 (Python Flask)",
  "author": "Twoje Imię",
  "version": "1.0.0"
}
```

### `GET /health`

```json
{
  "status": "OK",
  "timestamp": "2024-01-01T00:00:00.000000",
  "uptime": 3600.0
}
```

### `GET /api/todos`

```json
[
  {
    "id": 1,
    "title": "Stworzenie aplikacji Flask",
    "completed": true
  }
]
```

### `POST /api/todos`

```bash
curl -X POST http://localhost:5000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Nowe zadanie"}'
```

---

## 🧪 Testowanie

```bash
# Uruchomienie testów
pytest

# Testy z verbose
pytest -v

# Pokrycie kodu testami
pip install pytest-cov
pytest --cov=app --cov-report=html
```

Testy obejmują:

* testy jednostkowe endpointów
* integrację API Flask
* walidację odpowiedzi JSON
* obsługę błędów HTTP

---

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
curl http://localhost:5000/health
```

---

## ⚙️ CI/CD

GitHub Actions wykonuje:

1. **Testy**

   * Python 3.9 / 3.10 / 3.11
   * pytest + pokrycie kodu

2. **Build Dockera**

   * docker build + testy kontenera

3. **Deployment**

   * automatyczne wdrożenie z `main`
   * health check po deploymencie

---

## ☁️ Deployment

### Heroku

```bash
heroku create nazwaprojektu
echo "web: gunicorn app:app" > Procfile

git add Procfile
git commit -m "feat: dodanie Procfile"
git push heroku main
```

### AWS / Azure

Konfiguracja znajduje się w `.github/workflows/python-ci-cd.yml`

---

## 📚 Laboratoria

### Lab 1: Git/GitHub

* [x] Repozytorium
* [x] Commity
* [x] README.md
* [x] .gitignore

### Lab 2: Git Workflow

* [x] Branching
* [x] Pull Requesty
* [x] Merge conflicts
* [x] Tagowanie wersji
* [x] Testy jednostkowe

### Lab 3: CI/CD

* [x] GitHub Actions
* [x] Docker + Gunicorn
* [x] Automatyczne testy
* [x] Deployment
* [x] Health check

---

## 🛠️ Workflow Git

* `main` – produkcja
* `develop` – rozwój
* `feature/*` – nowe funkcje
* Pull Requesty + code review
* Semantic versioning

---

## 🤝 Contributing

1. Fork repo
2. `git checkout -b feature/nazwa`
3. `git commit -m 'feat: dodanie xyz'`
4. `git push origin feature/nazwa`
5. Stwórz Pull Request

---

## 📄 Licencja

Projekt objęty licencją [MIT](LICENSE).

---

## 🧑‍💻 Autor

**Klaudia Derlatka** – projekt zaliczeniowy z GIT 💙
GitHub: [@Dusiaxk](https://github.com/Dusiaxk)
