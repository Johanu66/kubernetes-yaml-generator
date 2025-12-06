def build_form_schema(resource_name, rules):
    resource = rules["resources"].get(resource_name)
    if not resource:
        raise ValueError(f"Resource {resource_name} non trouvée.")

    fields = resource["fields"]
    schema = []

    for name, config in fields.items():
        schema.append({
            "name": name,
            "type": config["type"],
            "label": config.get("label", name),
            "comment": config.get("comment", ""),
            "default": config.get("default", None),
            "options": config.get("options", None),
            "ui_control": config.get("ui_control", "text"),
            "placeholder": config.get("placeholder", ""),
            "level": config.get("level", "basic"),
        })

    return schema

