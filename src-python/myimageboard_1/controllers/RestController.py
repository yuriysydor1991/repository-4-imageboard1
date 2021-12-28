from .MainController import MainController
from myimageboard_1.models.ModelsFactory import ModelsFactory
from pyramid.view import view_config

class RestController(MainController):

    appName = 'MyImageBoard'
    appVersion = '1'
	
    def __init__(self, request):
        super().__init__(request)
        self.allowed_models = ['generalmodel'];
        
    @view_config(route_name='rest_v1', renderer='json')
    def rest_router(self):
        requestModel = self.request.matchdict['model']
        requestMethod = self.request.matchdict['method']
        
        realClass = requestModel + 'model'
        realModel = 'myimageboard_1.models'
        
        if realClass in self.allowed_models:
            modelsFactory = ModelsFactory()
            
            requestExecuttor = modelsFactory.getByName(realClass)
            
            if requestExecuttor != None and callable(getattr(requestExecuttor, requestMethod, None)):
                method_to_call = getattr(requestExecuttor, requestMethod)
                if (method_to_call != None):
                    result = method_to_call(self.request)
                    
                    return {
                        "app": self.appName,
                        "version": self.appVersion,
                        "status": 'success',
                        "content": result
                    }
        
        return {
            "app": self.appName,
            "version": self.appVersion,
            "status": 'error',
            "error" : "Invalid request"
        }
        
