from flask import Flask
from routes.form_routes import form_blueprint
from routes.yaml_routes import yaml_blueprint

def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False

    # Register blueprints
    app.register_blueprint(form_blueprint)
    app.register_blueprint(yaml_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.secret_key = "super_secret_key"
    app.run(debug=True)
