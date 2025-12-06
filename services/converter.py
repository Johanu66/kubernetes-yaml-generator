import yaml
from services.rules_loader import load_rules
from services.yaml_builder import apply_provider_overrides, replace_placeholders

rules = load_rules()


def convert_yaml_to_provider(yaml_input: str, target_provider: str):
    yaml_docs = list(yaml.safe_load_all(yaml_input))
    result_docs = []

    for doc in yaml_docs:
        if not doc or "kind" not in doc:
            result_docs.append(doc)
            continue

        kind = doc["kind"].lower()

        # --- Cas particulier PVC ---
        if kind == "persistentvolumeclaim":
            form_data = {
                "name": doc["metadata"].get("name", ""),
                "namespace": doc["metadata"].get("namespace", "default"),
                "storage": doc["spec"]["resources"]["requests"].get("storage", "1Gi")
            }

            template = rules["resources"]["pvc"]["template"]
            yaml_struct = replace_placeholders(template, form_data)

            overrides = rules["resources"]["pvc"].get("provider_overrides", {})
            converted = apply_provider_overrides(yaml_struct, overrides, target_provider)

            result_docs.append(converted)
            continue

        # --- Mode normal pour les autres ressources ---
        if kind not in rules["resources"]:
            result_docs.append(doc)
            continue

        resource_rules = rules["resources"][kind]

        cleaned = remove_provider_specific_data(doc)
        overrides = resource_rules.get("provider_overrides", {})
        converted = apply_provider_overrides(cleaned, overrides, target_provider)

        result_docs.append(converted)

    return yaml.dump_all(result_docs, sort_keys=False)



def remove_provider_specific_data(doc: dict):
    """Nettoie les annotations et champs liés à un provider cloud."""

    cleaned = yaml.safe_load(yaml.dump(doc))  # deep copy

    # --- Nettoyage annotations (Service, Ingress)
    if "metadata" in cleaned and "annotations" in cleaned["metadata"]:
        cleaned["metadata"]["annotations"] = {}

    # --- Nettoyage storageClassName (PVC)
    if cleaned.get("kind") == "PersistentVolumeClaim":
        if "spec" in cleaned and "storageClassName" in cleaned["spec"]:
            print("Avant nettoyage:", cleaned["spec"]["storageClassName"])
            cleaned["spec"]["storageClassName"] = None
            print("Après nettoyage:", cleaned["spec"]["storageClassName"])

    return cleaned
