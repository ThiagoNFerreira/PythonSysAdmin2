import flask
import sw.dados
import sw.naves

app = flask.Flask(__name__)  # dois underlines
app.register_blueprint(sw.naves.bp)

@app.route("/")
def home():
    dados = {"qualquer": "coisa"}
    return flask.jsonify(dados)

@app.route("/personagens")
def listar_personagens():
    return flask.jsonify(sw.personagens)

if __name__ == "__main__":  # também com 2 underlines
    sw.dados.setup()
    app.run(debug=True)
