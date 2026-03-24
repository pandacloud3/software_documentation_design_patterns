from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from app.routes import include_routes

db = SQLAlchemy()

def create_app() -> Flask:
    app = Flask(__name__)
    include_routes(app)
    return app
