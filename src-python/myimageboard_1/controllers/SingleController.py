from .MainController import MainController
from .MainController import MainController
from myimageboard_1.models.PostsModel import PostsModel
from pyramid.view import (view_config,view_defaults)

@view_defaults(renderer='../views/templates/single-post.pt')

class SingleController(MainController):

    posts = None
    
    def __init__(self, request = None):
        super().__init__(request)
        self.posts = PostsModel()
        
    @view_config(route_name='post')
    def single_post(self):
        #postUrl = self.request.params.get('post_url', None)
        postUrl = self.request.matchdict['post_url']

        if postUrl != None and len(postUrl) > 0:
            postData = self.posts.catalog_post(self.request, postUrl)
            if postData != None and "id" in postData:
                self.posts.incrementView(postData["id"])
                return {
                    "name": postData['title'],
                    "meta_keywords": postData['meta_keywords'],
                    "meta_description": postData['meta_description'],
                }
            
        return {
            "name" : "Post not found"
        }