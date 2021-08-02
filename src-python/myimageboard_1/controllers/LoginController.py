from .MainController import MainController
from myimageboard_1.models.UsersModel import UsersModel
from pyramid.view import (view_config,view_defaults)
import time

@view_defaults(renderer='../views/templates/login.pt')
class LoginController(MainController):
    def __init__(self, request):
        super().__init__(request)

    @view_config(route_name='login')
    def index(self):
        print(self.request.client_addr + ' ' + self.request.url)
        return {'name': 'Login page'}
    
    @view_config(route_name='signin')
    def login(self):
        print(self.request.client_addr + ' ' + self.request.url)
        
        time.sleep(1.1)
        
        username = self.request.params.get('login', '')
        password = self.request.params.get('password', '')
        
        print("Trying to login user: " + username)
        print("\t\twith password: " + password)
        
        user = self.users.getByUserPass(username, password)
        
        if user != None and "id" in user:
            print("There is user:")
            print(user)
            self.request.session['user_id'] = user['id']
            return {'name': 'Successfull login'}
            
        print("NO USER")
        
        return {'name': 'Failure to login'}