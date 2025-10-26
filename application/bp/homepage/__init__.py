# application/bp/homepage/__init__.py
from flask import Blueprint, render_template

# Blueprint object named "homepage" with its templates folder
homepage = Blueprint("homepage", __name__, template_folder="templates")

@homepage.route("/")
def home():
    return render_template("homepage.html")

@homepage.route("/about")
def about():
    return render_template("about.html")
