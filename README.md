# Aplicación Flask + MongoDB — Películas, Géneros y Usuarios

Proyecto académico de **Anyeli Mariana Cabezas Salamanca** ([@marialas](https://github.com/marialas)) — Tecnóloga ADSO SENA.

App Flask con MongoEngine: CRUD de películas por género + auth de usuarios. Incluye seed inicial y frontend Jinja.

## Stack
Python 3.10+, Flask 3, Flask-MongoEngine, Flask-CORS, python-dotenv, PyMongo, MongoDB Atlas/local.

## Estructura
```
app.py → factory, config MongoDB, seed admin/género/película
models/usuario.py, genero.py, pelicula.py
routes/usuario.py, genero.py, pelicula.py
templates/ + static/ → vistas
requirements.txt
```

## Instalación
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # completa SECRET_KEY, MONGODB_HOST, ADMIN_USER, ADMIN_PASSWORD, ADMIN_EMAIL
python app.py
```
Abre http://127.0.0.1:5000 — prueba con `peticiones.http`

## Seguridad
> v2026-09: se eliminó password hardcodeado en `app.py`, ahora todo por `.env`. No subas tu `.env` real.

## Autora
Tuluá, Colombia — abierta a remoto / Popayán. cabezasmari477@gmail.com
