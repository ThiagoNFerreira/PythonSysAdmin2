import flask
from bson.json_util import dumps

import sw.dados

bp = flask.Blueprint("naves", __name__, url_prefix="/naves")

@bp.route("")
def listar_naves():
    naves = dumps(list(sw.dados.naves()))
    return flask.Response(naves, headers=sw.dados.cabecalhos)

@bp.route("", methods=["POST"])
def criar_nave():
    nave = flask.request.json
    result = sw.dados.criar_nave(nave)
    return flask.jsonify({"id": str(result.inserted_id)})

@bp.route("/<int:id>")
def get_nave(id):
    nave = dumps(list(sw.dados.naves())[id])
    return flask.Response(nave, headers=sw.dados.cabecalhos)

@bp.route("/<int:id>", methods=["PUT"])
def modificar_nave(id):
    nave = flask.request.json
    naves = list(sw.dados.naves())
    nave_velha = naves[id]
    result = sw.dados.modificar_nave(
        {"_id": nave_velha["_id"]},
        nave
    )
    return flask.jsonify({
        "modificados": result.modified_count
    })