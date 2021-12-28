from myimageboard_1.models.MainModel import MainModel
from myimageboard_1.models.UsersModel import UsersModel

class MainController:

    def __init__(self, request = None):
        self.main = MainModel()
        self.users = UsersModel()
        
        if request != None:
            self.request = request
            self.session_signin()
        
    def session_signin(self):
        if hasattr(self, "request") and hasattr(self.request, "session") and "user_id" in self.request.session:
            self.users.signin(self.request.session['user_id'])
            
    def signed_user(self):
        return self.users.signed()

