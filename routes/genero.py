from flask import request, jsonify
from flask import render_template
from models.genero import Genero
from app import app
from utils import login_required

@app.route("/genero/", methods=['GET'])
@login_required
def listaGeneros():
    try:
        mensaje=None
        genero= Genero.objects()
        lista = []

        for g in genero:
            lista.append({
                "_id": str(g.id),
                "nombre": g.nombre
            })

        return jsonify({"generos": lista, "mensaje": mensaje}), 200
    
    except Exception as error:
        mensaje=str(error)

        return jsonify({"generos": lista, "mensaje": mensaje}), 200


@app.route("/genero/", methods=['POST'])
@login_required
def addGenero():
    try:
        mensaje=None
        estado=False
        if request.method=='POST':
            datos= request.get_json(force=True)
            genero= Genero(**datos)
            genero.save()
            estado=True
            mensaje="genero agregado correctamente"
            return jsonify({
                "estado": estado,
                "mensaje": mensaje,
                "genero": {
                    "_id": str(genero.id),
                    "nombre": genero.nombre
                }
            }), 201
        else:
            mensaje = "Método no permitido"
            return jsonify({"estado": estado, "mensaje": mensaje}), 405
    except Exception as error:
        return jsonify({"estado": False, "mensaje": str(error)}), 500
    
@app.route("/genero/<id>", methods=["PUT"])
@login_required
def updateGenero(id):
    try:
        datos = request.get_json(force=True)
        genero = Genero.objects(id=id).first()
        if genero:
            genero.update(**datos)
            return jsonify({"mensaje": "Género actualizado"}), 200
        else:
            return jsonify({"mensaje": "Género no encontrado"}), 404
    except Exception as error:
        return jsonify({"mensaje": str(error)}), 500


@app.route("/genero/<id>", methods=["DELETE"])
@login_required
def deleteGenero(id):
    try:
        genero = Genero.objects(id=id).first()
        if genero:
            genero.delete()
            return jsonify({"mensaje": "Género eliminado"}), 200
        else:
            return jsonify({"mensaje": "Género no encontrado"}), 404
    except Exception as error:
        return jsonify({"mensaje": str(error)}), 500


@app.route("/vistaListaGeneros")
@login_required
def vistaListaGeneros():
    return render_template("listarGeneros.html")

@app.route("/vistaAgregarGenero")
@login_required
def vistaAgregarGenero():
    return render_template("frmAgregarGenero.html")
