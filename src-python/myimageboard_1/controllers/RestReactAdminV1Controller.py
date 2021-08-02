from .MainController import MainController
from myimageboard_1.models.ModelsFactory import ModelsFactory
from myimageboard_1.models.PostsModel import PostsModel
from myimageboard_1.models.CommentsModel import CommentsModel
from pyramid.view import (view_config, view_defaults, render_view)
from pyramid.response import Response

class RestReactAdminV1Controller(MainController):
	
    def __init__(self, request):
        super().__init__(request)
        
    @view_config(route_name='rest_v1_react_admin', renderer="json")
    def rest_router(self):
        entitys = self.request.matchdict['entitys']
        if entitys == None:
            return {}
            
        if entitys == "users":
            allUsers = self.users.all()
            headerlist=[('X-Total-Count', str(len(allUsers) if allUsers != None else 0))]
            self.request.response.headerlist = headerlist
            return allUsers
            
        if entitys == "posts":
            posts=PostsModel()
            allPosts = posts.allReact(self.request)
            allPostsCnt = posts.allReact(self.request, True)
            headerlist=[('X-Total-Count', str(allPostsCnt if allPosts != None else 0))]
            self.request.response.headerlist = headerlist
            return allPosts
            
        if entitys == "comments":
            comments=CommentsModel()
            allComments = comments.allReactAdmin(self.request)
            allCommentsCnt = comments.allReactAdmin(self.request, True)
            headerlist=[('X-Total-Count', str(allCommentsCnt if allComments != None else 0))]
            self.request.response.headerlist = headerlist
            return allComments
        
        return {}