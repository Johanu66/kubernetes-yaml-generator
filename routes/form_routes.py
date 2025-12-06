from flask import Blueprint, render_template, request
from services.rules_loader import load_rules
from services.form_schema_builder import build_form_schema

form_blueprint = Blueprint("form", __name__)

rules = load_rules()


@form_blueprint.route("/")
def home():
    return render_template("home.html", resources=list(rules["resources"].keys()))


@form_blueprint.route("/form/<resource_name>")
def form(resource_name):
    schema = build_form_schema(resource_name, rules)
    providers = rules["providers"]

    return render_template("form.html", schema=schema, resource_name=resource_name, providers=providers)

@form_blueprint.route("/form/multi")
def form_multi():
    resource_list = list(rules["resources"].keys())
    providers = rules["providers"]
    return render_template("multi_form.html", resources=resource_list, providers=providers)

@form_blueprint.route("/form-fields/<resource_name>")
def form_fields(resource_name):
    schema = build_form_schema(resource_name, rules)
    return schema  # Flask renvoie automatiquement du JSON
