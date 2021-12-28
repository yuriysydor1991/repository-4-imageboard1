from .GeneralSubModel import GeneralSubModel

class GeneralModel:
    def __init__(self):
        self.main = GeneralSubModel()
        pass
        
    def home_content(self, request):
        posts = self.main.catalog_posts(request)
        rt = {} 
        
        if posts != None:      
          rt = {
              'posts': posts,
              'pagination': posts["pagination"]
          }
        
        return rt
        
    def signin_content(self, request):
        return self.main.signin_content(request)
        
    def post_content(self, request):
        return self.main.post_content(request, request.params.get('post_url', None))

    def post_comments(self, request):
        post = self.main.catalog_post(request, request.params.get('post_url', None))
        return self.main.post_comments(request, post['id'])
    
