from flask import Flask, session
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Cargar variables desde .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
CORS(app)

# Configuración de MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': os.getenv("MONGODB_NAME"),
    'host': os.getenv("MONGODB_HOST"),
    'port': int(os.getenv("MONGODB_PORT"))
}

db = MongoEngine(app)

# Importar modelos
from models.usuario import Usuario
from models.genero import Genero
from models.pelicula import Pelicula

# Importación de rutas
from routes.genero import *
from routes.pelicula import *
from routes.usuario import *

# Crear usuario si no existe
if not Usuario.objects(usuario="admin").first():
    Usuario(
        usuario="admin",
        password="123",
        nombre="Administrador",
        correo="admin@ejemplo.com"
    ).save()
    print("✔ Usuario admin creado")
else:
    print("ℹ Usuario admin ya existe")

# Crear género si no existe
if not Genero.objects(nombre="Acción"):
    Genero(nombre="Acción").save()
    print("✔ Género Acción creado")

# Crear película si no existe
genero = Genero.objects(nombre="Acción").first()
if genero and not Pelicula.objects(codigo=101):
    Pelicula(
        codigo=101,
        titulo="Rápido y Furioso",
        protagonista="Vin Diesel",
        duracion=120,
        resumen="Película de carreras",
        foto="img.jpg",
        genero=genero
    ).save()
    print("✔ Película creada")



from flask import render_template

@app.route("/")
def inicio():
    if "usuario" not in session:
        return render_template("login.html")
    return render_template("contenido.html")
   
