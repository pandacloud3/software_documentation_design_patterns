from app.bll.app_bll.i_app_bll import IAppBLL
from app.dal.app_dal.i_app_dal import IAppDAL

class AppBLL(IAppBLL):
    def __init__(self, dal: IAppDAL):
        self.dal = dal

    def create_db(self):
        data = self.dal.read_csv()
        self.dal.create_db()
        self.dal.write_db(data)
