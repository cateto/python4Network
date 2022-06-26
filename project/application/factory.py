from flask import Flask
from application.api.index import index

def create_app():
    app = Flask(__name__)
    app.register_blueprint(index)

    return app