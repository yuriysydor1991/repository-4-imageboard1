from .MainController import MainController
from pyramid.view import (view_config, view_defaults)

@view_defaults(renderer='../views/templates/react-admin-app.pt')

class ReactAdminController(MainController):

    def __init__(self, request):
        super().__init__(request)
        
    @view_config(route_name='reactadmin')
    def application (self):
        return {
            "name": "Admin on react"
        }
        
    