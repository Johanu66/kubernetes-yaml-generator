from flask import Blueprint, render_template, request
from services.converter import convert_yaml_to_provider
from services.rules_loader import load_rules

converter_blueprint = Blueprint("converter", __name__)

rules = load_rules()

@converter_blueprint.route("/convert", methods=["GET", "POST"])
def convert_yaml():
    if request.method == "GET":
        return render_template("convert.html", providers=rules["providers"])

    yaml_input = request.form["yaml_input"]
    target_provider = request.form["target_provider"]

    output = convert_yaml_to_provider(yaml_input, target_provider)

    return render_template("preview.html", yaml_output=output)
