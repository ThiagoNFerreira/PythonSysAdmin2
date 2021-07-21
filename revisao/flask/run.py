import flask as f
import loja.blueprint
from config.db import setup

app = f.Flask(__name__)
app.register_blueprint(loja.blueprint.bp)

@app.route("/")
def index():
    return f.render_template("index.html")

if __name__ == "__main__":
    setup()
    app.run(debug=True)