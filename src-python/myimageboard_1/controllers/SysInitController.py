from .MainController import MainController
from myimageboard_1.models.InitModel import InitModel
from pyramid.view import (view_config,view_defaults)


@view_defaults(renderer='../views/templates/sysinit.pt')
class SysInitController(MainController):
    def __init__(self, request):
        super().__init__(request)
        self.model = InitModel()

    @view_config(route_name='sysinit')
    def sysinit(self):
        print(self.request.client_addr + ' ' + self.request.url)
        self.model.initBD()
        return {'name': 'SysInit script'}