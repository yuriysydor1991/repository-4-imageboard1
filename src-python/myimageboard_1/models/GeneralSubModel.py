from .PostsModel import PostsModel
from .CommentsModel import CommentsModel
from .UsersModel import UsersModel

class GeneralSubModel(PostsModel, CommentsModel, UsersModel):
    def __init__(self):
        super().__init__()
        
    def signin_content(self, request):
        return {
            "user": self.cleanedUser()
        }
        
    def post_content(self, request = None, postUrl = None):
        if request == None:
            return None
            
        return {
            "posts": self.catalog_post_ext(request, postUrl)
        }

    def post_comments(self, request, postId):
        return self.allByPost(postId, request)