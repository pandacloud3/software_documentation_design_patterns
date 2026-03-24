from flask import Flask
from app.routes.orders.patient_routes import patient_routes

def include_routes(app: Flask):
    app.register_blueprint(patient_routes)
