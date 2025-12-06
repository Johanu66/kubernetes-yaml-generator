def build_form_schema(resource_name, rules):
    """Construit la structure du formulaire pour un type de ressource."""

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
            "item": config.get("item", None)
        })

    return schema
