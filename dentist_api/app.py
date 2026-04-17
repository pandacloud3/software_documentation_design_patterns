from flask import Flask
from core.models import db
from dal.repository import SqlRepository
from bll.service import ClinicService
from presentation.routes import api_blueprint, init_routes

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:VladPanda777@localhost:3306/dentistry_db'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    repository = SqlRepository()
    service = ClinicService(repository)
    init_routes(service)
    
    app.register_blueprint(api_blueprint)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)