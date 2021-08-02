from .MainController import MainController
from pyramid.view import (view_config, view_defaults)

@view_defaults(renderer='../views/templates/home.pt')

class HomeController(MainController):
    def __init__(self, request):
        super().__init__(request)

    @view_config(route_name='home')
    def home(self):
        print(self.request.client_addr + ' ' + self.request.url)
        return {'name': 'Home'}