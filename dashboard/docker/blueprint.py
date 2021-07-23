from typing import Collection
from docker.api import container
import flask as f
import docker

bp = f.Blueprint("docker", __name__, url_prefix="/docker")
client = docker.DockerClient()

@bp.route("")
def index():
    print(f.current_app.logger.level)
    f.current_app.logger.info("listando containers do docker")
    cs = client.containers.list(all=True)
    return f.render_template(
        "docker/index.html",
        containers=cs)

@bp.route("/<id>/executar")
def start_container(id):
    container = client.containers.get(id)
    f.current_app.logger.info(f"startando {container.name}")
    container.start()
    f.flash(f"{container.name} startado", "info")
    return f.redirect(f.url_for('docker.index'))

@bp.route("/<id>/parar")
def stop_container(id):
    container = client.containers.get(id)
    f.current_app.logger.info(f"parando {container.name}")
    container.stop()
    f.flash(f"{container.name} stopado", "warn")
    return f.redirect(f.url_for('docker.index'))

@bp.route("/<id>/remover")
def remove_container(id):
    container = client.containers.get(id)
    f.current_app.logger.info(f"removendo {container.name}")
    container.remove()
    return f.redirect(f.url_for('docker.index'))