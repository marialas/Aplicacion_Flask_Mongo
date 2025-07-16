from models.usuario import Usuario
from utils.email import enviarCorreo
import random
import string
from flask import request, jsonify, session
from app import app


@app.route("/login", methods=['POST'])
def login():
    datos = request.get_json(force=True)
    usuario = Usuario.objects(usuario=datos.get("usuario"), password=datos.get("password")).first()
    if usuario:
        session["usuario"] = usuario.usuario
        return jsonify({"estado": True, "mensaje": "Inicio de sesión exitoso"}), 200
    else:
        return jsonify({"estado": False, "mensaje": "Credenciales incorrectas"}), 401

@app.route("/logout", methods=["GET"])
def logout():
    session.pop("usuario", None)
    return jsonify({"mensaje": "Sesión cerrada"}), 200

@app.route("/recuperar", methods=["POST"])
def recuperar():
    datos = request.get_json(force=True)
    usuario = Usuario.objects(usuario=datos.get("usuario")).first()

    if not usuario:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    # Generar nueva contraseña
    nueva = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    usuario.update(password=nueva)

    # Enviar correo con la nueva contraseña
    enviarCorreo(usuario.correo, "Nueva contraseña", f"Tu nueva contraseña es: {nueva}")

    return jsonify({"mensaje": "Contraseña actualizada y enviada por correo"}), 200
