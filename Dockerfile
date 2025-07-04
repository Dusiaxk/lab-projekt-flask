# Dockerfile dla aplikacji Python Flask
FROM python:3.11-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie requirements.txt
COPY requirements.txt .

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie kodu aplikacji
COPY . .

# Eksponowanie portu
EXPOSE 5000

# Tworzenie użytkownika nieuprzywilejowanego
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app
USER appuser

# Komenda uruchomieniowa
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"] 