import yaml


def build_yaml_from_template(resource_name, rules, form_data, provider_name):
    resource_rules = rules["resources"][resource_name]
    template = resource_rules["template"]

    # 1. Créer structure YAML avec variables remplacées
    yaml_structure = replace_placeholders(template, form_data)

    # 2. Appliquer les overrides du provider
    yaml_structure = apply_provider_overrides(
        yaml_structure,
        resource_rules.get("provider_overrides", {}),
        provider_name
    )

    return yaml.dump(yaml_structure, sort_keys=False)


def replace_placeholders(obj, form_data):
    """Remplace les variables $xxx dans le template par les valeurs utilisateur."""

    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            if isinstance(value, str) and value.startswith("$"):
                variable = value[1:]
                new_dict[key] = form_data.get(variable)
            else:
                new_dict[key] = replace_placeholders(value, form_data)
        return new_dict

    if isinstance(obj, list):
        return [replace_placeholders(item, form_data) for item in obj]

    return obj


def apply_provider_overrides(yaml_struct, overrides, provider_name):
    """Injecte les overrides selon le provider dans le YAML final."""

    provider_data = overrides.get(provider_name)
    if not provider_data:
        return yaml_struct

    # --- Normalisation: s'assurer que metadata.annotations existe et est un dict ---
    yaml_struct.setdefault("metadata", {})

    annotations = yaml_struct["metadata"].get("annotations")

    # Si annotations est une string, None ou autre → convertir en dict
    if not isinstance(annotations, dict):
        yaml_struct["metadata"]["annotations"] = {}
    else:
        yaml_struct["metadata"]["annotations"] = annotations.copy()

    # --- Cas 1 : ajouter les annotations provider ---
    if "annotations" in provider_data:
        for key, value in provider_data["annotations"].items():
            yaml_struct["metadata"]["annotations"][key] = value

    # --- Cas 2 : StorageClassName (PVC)
    if "storageClassName" in provider_data:
        yaml_struct.setdefault("spec", {})
        yaml_struct["spec"]["storageClassName"] = provider_data["storageClassName"]

    # --- Cas 3 : autres extensions futures ---
    for key, value in provider_data.items():
        if key not in ["annotations", "storageClassName"]:
            yaml_struct[key] = value

    return yaml_struct
