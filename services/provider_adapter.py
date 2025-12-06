def apply_provider_overrides(resource_dict, resource_rules, provider_name):
    overrides = resource_rules.get("provider_specific", {}).get(provider_name, {})

    # Exemple : ajouter des annotations propres au cloud
    if "supported_annotations" in overrides:
        resource_dict["metadata"].setdefault("annotations", {})

    return resource_dict
