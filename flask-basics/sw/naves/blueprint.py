import flask
from bson.json_util import dumps
# from sw.naves import models
from . import models # ^^^ mesma coisa
from config.api import cabecalhos

bp = flask.Blueprint("naves", __name__, url_prefix="/naves")

@bp.route("")
def listar_naves():
    naves = dumps(list(models.get_naves()))
    return flask.Response(naves, headers=cabecalhos)

@bp.route("", methods=["POST"])
def criar_nave():
    nave = flask.request.json
    result = models.criar_nave(nave)
    return flask.jsonify({"id": str(result.inserted_id)})

@bp.route("/<int:id>")
def get_nave(id):
    nave = dumps(list(models.get_naves())[id])
    return flask.Response(nave, headers=cabecalhos)

@bp.route("/<int:id>", methods=["PUT"])
def modificar_nave(id):
    nave = flask.request.json
    naves = list(models.get_naves())
    nave_velha = naves[id]
    result = models.modificar_nave(
        {"_id": nave_velha["_id"]},
        nave
    )
    return flask.jsonify({
        "modificados": result.modified_count
    })