from flask import Flask

from .routes import register_routes


def create_app(config_object: str | None = None) -> Flask:
    """Application factory for the content-matrix Flask app."""
    app = Flask(__name__)

    if config_object:
        app.config.from_object(config_object)

    # Allow overriding config with environment variables prefixed by FLASK_
    app.config.from_prefixed_env()

    register_routes(app)
    return app

