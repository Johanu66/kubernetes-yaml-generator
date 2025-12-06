from flask import Blueprint, render_template, request, send_file, session
from services.rules_loader import load_rules
from services.yaml_builder import build_yaml_from_template
import tempfile
import os

yaml_blueprint = Blueprint("yaml", __name__)
rules = load_rules()


@yaml_blueprint.route("/generate", methods=["POST"])
def generate_yaml():
    form_data = request.form.to_dict(flat=True)
    resource_name = form_data.pop("resource_name")
    provider_name = form_data.pop("provider_name")

    yaml_output = build_yaml_from_template(resource_name, rules, form_data, provider_name)

    # Save YAML to session for download
    session["generated_yaml"] = yaml_output
    session["filename"] = f"{resource_name}.yaml"

    return render_template("preview.html", yaml_output=yaml_output)


@yaml_blueprint.route("/download")
def download_yaml():
    yaml_data = session.get("generated_yaml", "")
    filename = session.get("filename", "config.yaml")

    # Create temporary file
    temp_path = os.path.join(tempfile.gettempdir(), filename)
    with open(temp_path, "w") as f:
        f.write(yaml_data)

    return send_file(temp_path, as_attachment=True, download_name=filename)


@yaml_blueprint.route("/generate-multi", methods=["POST"])
def generate_multi_yaml():
    provider = request.form.get("provider_name")

    # Reconstituer le JSON complet
    resources = []
    for key, value in request.form.items():
        if key.startswith("resources["):
            parts = key.split("][")
            index = int(parts[0].replace("resources[", "").replace("]", ""))
            field = parts[1].replace("]", "")

            # Ensure index exists
            while len(resources) <= index:
                resources.append({})

            resources[index][field] = value

    # Génération
    outputs = []
    for r in resources:
        resource_type = r.pop("type")
        yaml_output = build_yaml_from_template(resource_type, rules, r, provider)
        outputs.append(yaml_output)

    # Concatène les YAML avec ---
    final_yaml = "\n---\n".join(outputs)

    session["generated_yaml"] = final_yaml
    session["filename"] = f"kubernetes_bundle.yaml"

    return render_template("preview.html", yaml_output=final_yaml)
