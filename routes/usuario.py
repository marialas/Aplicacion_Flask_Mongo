from models.usuario import Usuario
from utils.email import enviarCorreo
import random
import string
from flask import request, jsonify, session, render_template

def registrar_rutas_usuario(app):

    @app.route("/")
    def inicio():
        if "usuario" not in session:
            return render_template("login.html")
        return render_template("contenido.html")

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
        return render_template("logout.html")

    @app.route("/recuperar", methods=["POST"])
    def recuperar():
        datos = request.get_json(force=True)
        usuario = Usuario.objects(usuario=datos.get("usuario")).first()

        if not usuario:
            return jsonify({"mensaje": "Usuario no encontrado"}), 404

        nueva = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        usuario.update(password=nueva)

        enviarCorreo(usuario.correo, "Nueva contraseña", f"Tu nueva contraseña es: {nueva}")
        return jsonify({"mensaje": "Contraseña actualizada y enviada por correo"}), 200

    @app.route("/recuperar", methods=["GET"])
    def vista_recuperar():
        return render_template("recuperar.html")
    
    @app.route("/vistaRegistrar")
    def vistaRegistrar():
        return render_template("registro.html")

    @app.route("/registrar", methods=["POST"])
    def registrar_usuario():
        datos = request.get_json(force=True)
        if Usuario.objects(usuario=datos["usuario"]).first():
            return jsonify({"mensaje": "El usuario ya existe"}), 400

        Usuario(
            usuario=datos["usuario"],
            password=datos["password"],
            nombre=datos["nombre"],
            correo=datos["correo"]
        ).save()

        return jsonify({"mensaje": "Usuario registrado exitosamente"}), 200

    @app.route("/vistaUsuarios")
    def vistaUsuarios():
        return render_template("usuarios.html")
