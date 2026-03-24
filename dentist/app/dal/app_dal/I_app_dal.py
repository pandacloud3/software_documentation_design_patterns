from abc import ABC, abstractmethod

class IAppDAL(ABC):
    @abstractmethod
    def read_csv(self):
        pass

    @abstractmethod
    def create_db(self):
        pass

    @abstractmethod
    def write_db(self):
        pass

    # """
    #     Initializes DB with SQLAlchemy
    #     :param app: Flask application object
    #     """
    # db.init_app(app)
    #
    # if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
    #     create_database(app.config[SQLALCHEMY_DATABASE_URI])
    #
    # import my_project.auth.domain
    # with app.app_context():
    #     db.create_all()
