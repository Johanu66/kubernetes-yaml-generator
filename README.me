# Kubernetes YAML Generator  

**Générateur visuel et convertisseur de configurations Kubernetes (YAML)**

Site en production :
🌐 [https://kubernetes-yaml-generator.randever.com](https://kubernetes-yaml-generator.randever.com)

---

## Objectif

Ce projet a pour objectif de rendre **la création et la conversion de fichiers YAML Kubernetes extrêmement simple**, même pour les débutants.

Grâce à une interface web intuitive, l'utilisateur peut :

- Générer des ressources Kubernetes sans connaître la syntaxe YAML  
- Créer plusieurs ressources en un seul fichier  
- Convertir un fichier YAML d’un provider cloud à un autre (AWS → GCP → Azure)  
- Générer automatiquement les bonnes annotations et options selon le provider  
- Exporter ou copier le YAML généré

Ce projet est un excellent outil pédagogique pour l’apprentissage de Kubernetes et une base solide pour la génération automatisée de manifests.

---

## Fonctionnalités principales

### ✔ Génération de ressource unitaire
Créer une ressource parmi :
- Deployment  
- Service  
- Ingress  
- ConfigMap  
- Secret  
- PersistentVolumeClaim  

Chaque champ du formulaire :
- est pré-rempli  
- possède une aide contextuelle  
- propose des valeurs simples à choisir  
- masque les options avancées par défaut  

---

### ✔ Génération multi-ressources
Permet de :
- construire plusieurs objets Kubernetes dans une seule interface  
- ajouter/supprimer des modules dynamiquement  
- générer un YAML multi-document propre et cohérent  

---

### ✔ Conversion YAML → Provider
Convertit automatiquement un fichier YAML pour correspondre aux spécificités des providers :

| Provider | Ajustements automatiques |
|---------|---------------------------|
| **AWS** | annotations ELB, storageClass gp2, etc. |
| **GCP** | annotations GCE, storageClass standard-rwo |
| **Azure** | annotations AGIC, storageClass managed-premium |

Le système nettoie le YAML avant conversion afin d’éviter la contamination entre providers.

---

### ✔ Interface web élégante et moderne
Le projet inclut :
- UI responsive  
- Formulaires intelligents  
- Bouton “Copier YAML”  
- Pages organisées en sections et cartes  
- YAML preview colorée  

---

## Architecture du projet

```
/app
/db
    rules.json        → Contient toutes les règles de génération et overrides providers
/routes
    form_routes.py    → Formulaires et pages UI
    yaml_routes.py    → Génération YAML
    converter_routes.py→ Conversion YAML entre providers
/services
    yaml_builder.py   → Génération de YAML depuis templates
    converter.py       → Nettoyage + conversion inter-provider
/templates
    *.html             → Templates Jinja2
/static
/css/style.css     → Styles UI modernes
    app.py                 → Application Flask (WSGI compatible)
    passenger_wsgi.py      → Entrée WSGI pour serveur Passenger
````

---

## Installation locale

### 1. Cloner le projet
```bash
git clone https://github.com/.../kubernetes-yaml-generator.git
cd kubernetes-yaml-generator
````

### 2. Installer les dépendances

Créer un environnement virtuel :

```bash
python3 -m venv venv
source venv/bin/activate
```

Installer les modules :

```bash
pip install -r requirements.txt
```

### 3. Lancer l’application

```bash
python app.py
```

L'application sera disponible sur :

```
http://localhost:5000
```

---

## Fichier rules.json

Toute la logique de génération est centralisée dans :

```
db/rules.json
```

Il contient :

* liste des ressources
* champs UI dynamiques
* templates YAML
* valeurs par défaut
* annotations providers
* overrides provider (AWS / GCP / Azure)

---

## Contribution

Les contributions sont les bienvenues !
Vous pouvez proposer :

* Ajout de nouvelles ressources Kubernetes
* Ajout de nouveaux providers (Alibaba, DigitalOcean…)
* Amélioration UI/UX
* Optimisation du système de conversion

Pour contribuer :

```bash
git checkout -b feature/ma-feature
git commit -m "Ajout d’une nouvelle fonctionnalité"
git push origin feature/ma-feature
```

---

## Licence

Ce projet est distribué sous licence **MIT**, ce qui permet une utilisation libre, commerciale ou éducative.

---

## Auteur

Projet développé par Johanu GANDONOU, Paul ARAGO et Alexis GEORGES, dans le cadre du cours **Programmation Objet Avancée – UQAC**.

Site en production :
🌐 [https://kubernetes-yaml-generator.randever.com](https://kubernetes-yaml-generator.randever.com)

