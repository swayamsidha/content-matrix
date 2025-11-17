from flask import Blueprint, jsonify


api = Blueprint("api", __name__)


@api.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})


def register_routes(app):
    app.register_blueprint(api)

