import yaml

def build_yaml_from_template(resource_name, rules, form_data, provider_name):
    resource_rules = rules["resources"][resource_name]
    template = resource_rules["template"]

    yaml_structure = replace_placeholders(template, form_data, provider_name)

    return yaml.dump(yaml_structure, sort_keys=False)


def replace_placeholders(obj, form_data, provider_name):
    """Remplace les variables $xxx par les valeurs dans form_data."""

    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            if isinstance(value, str) and value.startswith("$"):
                variable = value[1:]
                new_dict[key] = form_data.get(variable)
            else:
                new_dict[key] = replace_placeholders(value, form_data, provider_name)
        return new_dict

    if isinstance(obj, list):
        return [replace_placeholders(item, form_data, provider_name) for item in obj]

    return obj
