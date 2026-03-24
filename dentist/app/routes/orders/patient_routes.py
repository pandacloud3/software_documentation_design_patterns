from flask import Blueprint

patient_routes = Blueprint('patient', __name__)

@patient_routes.get('/')
def index():
    return 'patient Routes'
