from os import name
import flask as f
import jenkins

bp = f.Blueprint("jenkins", __name__, url_prefix="/jenkins")
client = jenkins.Jenkins("http://localhost:8080", username="admin", password="loca1020")

@bp.route("")
def index():
    job_list = client.get_jobs()
    job_list = [client.get_job_info(j["name"])for j in job_list]
    return f.render_template("jenkins/index.html", jobs=job_list)

@bp.route("/<nome>/editar")
def edit_job(nome):
    config = client.get_job_config(name)
    return f.render_template("jenkins/edit")