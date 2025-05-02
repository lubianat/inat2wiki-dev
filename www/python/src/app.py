import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request
from flask_bootstrap import Bootstrap5
from wdcuration import lookup_id
from inat2wiki.parse_observation import get_commons_url, request_observation_data

# Load .env into os.environ
load_dotenv()

app = Flask(__name__)
# Pull SECRET_KEY from env (will raise if missing)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

Bootstrap5(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/parse/", methods=["GET", "POST"])
@app.route("/parse", methods=["GET", "POST"])
def parse_obs_base():
    if request.method == "POST":
        obs_id = request.form.get("obs_id")
        return redirect(f"/parse/{obs_id}")
    return render_template("parse.html")


@app.route("/parse/<observation_id>", methods=["GET", "POST"])
def parse_obs(observation_id):
    observation_data = request_observation_data(observation_id)
    qid = lookup_id(
        observation_data["taxon"]["min_species_taxon_id"], "P3151", default=""
    )
    for photo in observation_data["photos"]:
        upload_url = get_commons_url(observation_data, photo, observation_id)
        photo["url"] = photo["url"].replace("square", "original")
        photo["upload_url"] = upload_url or "License not supported"
    return render_template("parse.html", observation_data=observation_data, qid=qid)


@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500
