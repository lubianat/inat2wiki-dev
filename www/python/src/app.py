"""A flask app to connect iNaturalist to Wikidata."""

from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wdcuration import get_statement_values, lookup_id
from wtforms import BooleanField, IntegerField, StringField
from wtforms.validators import InputRequired, Optional

import flask
from flask import Flask, redirect, render_template, request
import requests

from inat2wiki.parse_observation import get_commons_url, request_observation_data

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
Bootstrap5(app)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/about")
def about():
    return flask.render_template("about.html")


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
    photo_data_list = observation_data["photos"]
    qid = lookup_id(
        observation_data["taxon"]["min_species_taxon_id"], "P3151", default=""
    )
    for i, photo_data in enumerate(photo_data_list):
        upload_url = get_commons_url(observation_data, photo_data, observation_id)
        observation_data["photos"][i]["url"] = observation_data["photos"][i][
            "url"
        ].replace("square", "original")
        observation_data["photos"][i]["upload_url"] = upload_url
        if upload_url == "License not supported":
            observation_data["photos"][i]["upload_url"] = "License not supported"
    return render_template("parse.html", observation_data=observation_data, qid=qid)


@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500
