import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, g, session, url_for
from flask_bootstrap import Bootstrap5
from flask_babel import Babel, gettext as _

from wdcuration import lookup_id
from inat2wiki.parse_observation import get_commons_url, request_observation_data

__version__ = "0.1.0"

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["BABEL_DEFAULT_LOCALE"] = "en"
app.config["BABEL_TRANSLATION_DIRECTORIES"] = "translations"

# Initialize extensions
Bootstrap5(app)

SUPPORTED_LANGUAGES = ["en", "es", "pt"]


# Define the locale selector function
def get_locale():
    # Check for language in URL parameters
    lang = request.args.get("lang")
    if lang in SUPPORTED_LANGUAGES:
        session["lang"] = lang
        return lang
    # Check for language in session
    if (lang := session.get("lang")) in SUPPORTED_LANGUAGES:
        return lang
    # Fallback to browser's accepted languages
    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)


# Initialize Babel with the locale selector
babel = Babel(app, locale_selector=get_locale)


# Store selected locale in g.locale for templates
@app.before_request
def before_request():
    g.locale = get_locale()


@app.route("/set-lang/<lang>")
def set_lang(lang):
    if lang in SUPPORTED_LANGUAGES:
        session["lang"] = lang
    return redirect(request.referrer or url_for("index"))


@app.route("/")
def index():
    greeting = _("Welcome to iNat2Wiki!")
    return render_template("index.html", greeting=greeting)


@app.route("/about")
def about():
    title = _("About iNat2Wiki")
    return render_template("about.html", title=title)


@app.route("/parse/", methods=["GET", "POST"])
@app.route("/parse", methods=["GET", "POST"])
def parse_obs_base():
    if request.method == "POST":
        obs_id = request.form.get("obs_id")
        if "www.inaturalist.org/observations/" in obs_id:
            obs_id = obs_id.split("/observations/")[-1]
        return redirect(url_for("parse_obs", observation_id=obs_id))
    title = _("Parse observation")
    return render_template("parse.html", title=title)


@app.route("/parse/<observation_id>", methods=["GET", "POST"])
def parse_obs(observation_id):
    observation_data = request_observation_data(observation_id)
    qid = lookup_id(
        observation_data["taxon"]["min_species_taxon_id"], "P3151", default=""
    )
    for photo in observation_data["photos"]:
        upload_url = get_commons_url(observation_data, photo, observation_id)
        photo["url"] = photo["url"].replace("square", "original")
        photo["upload_url"] = upload_url or _("License not supported")
    title = _("Observation Details")
    return render_template(
        "parse.html", observation_data=observation_data, qid=qid, title=title
    )


@app.errorhandler(404)
def not_found_error(error):
    message = _("Page not found")
    return render_template("404.html", message=message), 404


@app.errorhandler(500)
def internal_error(error):
    message = _("An internal error occurred")
    return render_template("500.html", message=message), 500


if __name__ == "__main__":
    app.run(debug=True)
