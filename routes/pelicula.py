from flask import request, jsonify
from flask import render_template
from models.pelicula import Pelicula
from models.genero import Genero
from app import app
from utils.utils import login_required


@app.route("/pelicula/", methods=['GET'])
@login_required
def listaPelicula():
    try:
        mensaje=None
        pelicula= Pelicula.objects()
    except Exception as error:
        mensaje=str(error)

    return{"mensaje": mensaje, "peliculas":pelicula}

@app.route("/pelicula/", methods=["POST"])
@login_required
def addPelicula():
    try:
        datos = request.get_json(force=True)
        genero = Genero.objects(id=datos["genero"]).first()
        if not genero:
            return jsonify({"mensaje": "Género no encontrado"}), 404
        datos["genero"] = genero
        pelicula = Pelicula(**datos).save()
        return jsonify({"mensaje": "Película creada", "id": str(pelicula.id)}), 201
    except Exception as error:
        return jsonify({"mensaje": str(error)}), 500
    
    
@app.route("/pelicula/<id>", methods=['GET'])
@login_required
def getPelicula(id):
    try:
        pelicula = Pelicula.objects(id=id).first()
        if not pelicula:
            return jsonify({"mensaje": "Película no encontrada"}), 404

        return jsonify({
            "id": str(pelicula.id),
            "codigo": pelicula.codigo,
            "titulo": pelicula.titulo,
            "protagonista": pelicula.protagonista,
            "duracion": pelicula.duracion,
            "resumen": pelicula.resumen,
            "foto": pelicula.foto,
            "genero": str(pelicula.genero.id)
        }), 200
    except Exception as error:
        return jsonify({"mensaje": str(error)}), 500


@app.route("/pelicula/<id>", methods=['PUT'])
@login_required
def updatePelicula(id):
    try:
        datos = request.get_json(force=True)
        pelicula = Pelicula.objects(id=id).first()
        if not pelicula:
            return jsonify({"mensaje": "Película no encontrada"}), 404

        if "genero" in datos:
            genero = Genero.objects(id=datos["genero"]).first()
            if genero:
                datos["genero"] = genero

        pelicula.update(**datos)
        return jsonify({"mensaje": "Película actualizada"}), 200

    except Exception as error:
        return jsonify({"mensaje": str(error)}), 500


@app.route("/pelicula/<id>", methods=["DELETE"])
@login_required
def deletePelicula(id):
    try:
        pelicula = Pelicula.objects(id=id).first()
        if pelicula:
            pelicula.delete()
            return jsonify({"mensaje": "Película eliminada"}), 200
        else:
            return jsonify({"mensaje": "Película no encontrada"}), 404
    except Exception as error:
        return jsonify({"mensaje": str(error)}), 500
    


@app.route("/vistaListaPeliculas")
@login_required
def vistaListaPeliculas():
    return render_template("listarPeliculas.html")

@app.route("/vistaAgregarPelicula")
@login_required
def vistaAgregarPelicula():
    generos = Genero.objects()
    return render_template("frmAgregarPelicula.html", generos=generos)

@app.route("/vistaEditarPelicula/<id>")
@login_required
def vistaEditarPelicula(id):
    pelicula = Pelicula.objects(id=id).first()
    generos = Genero.objects()
    if not pelicula:
        return "Película no encontrada", 404
    return render_template("frmEditarPelicula.html", pelicula=pelicula, generos=generos)

