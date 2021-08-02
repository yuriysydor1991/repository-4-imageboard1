from .MainModel import MainModel
from .UsersModel import UsersModel
from .CommentsModel import CommentsModel
import math

class PostsModel(MainModel):
    table = "posts"
    pagination_disp = 3
    
    def all (self):
        myT = self.tablename(PostsModel.table)
        query = "SELECT * FROM " + myT + " ORDER BY id DESC;"
        
        posts = self.query_get(query)
        
        for post in posts:
            self.prepare_post_raw(post)
            
        return posts
        
    def allReact (self, request, count = False):
        #def build_catalog_query(self, limit=10, offset=0, order="date", 
        #                        direction="DESC", search=None, count = False, postUrl = None, noJoins=False):
        start = int(request.params.get('_start', 0))
        end = int(request.params.get('_end', 10))
        order = request.params.get('_sort', 'date')
        limit = end - start
        offset = start
        direction = request.params.get('_order', 'desc')
        
        query = self.build_catalog_query(
            noJoins=True,
            limit=limit,
            offset=offset,
            order=order,
            direction=direction,
            count=count
        )
        
        if count:
            dbr = self.query_get_single(query)
            return dbr['posts_count'] if dbr != None and "posts_count" in dbr else 0
        
        posts = self.query_get(query)
        
        for post in posts:
            self.prepare_post_raw(post)
            
        return posts
    
    def incrementView(self, postId = None):
        if postId == None:
            return 
        myT = self.tablename(PostsModel.table)
        query = "UPDATE " + myT + " SET views = views + 1 WHERE id = " + str(postId) + ";"

        self.query(query)

    def catalog_post (self, request = None, postUrl = None):
        query = self.build_catalog_query(postUrl = postUrl)
        post = self.query_get_single(query)
        
        if (post == None):
            return None
        
        self.prepare_post(post, request)

        comments = CommentsModel()
        res = comments.allByPost(post['id'], request, True)
        post['comments'] = res['comments_count']
        
        return post
        
    def catalog_post_ext (self, request = None, postUrl = None):
        post = self.catalog_post(request, postUrl)
        
        return {
            "list": [post],
            "all_count": 1 if post != None else 0
        }
        
    def prepare_post_raw(self, post = None):
        post['date'] = post['date'].strftime(MainModel.globalDateFormat)
        post['updated'] = post['updated'].strftime(MainModel.globalDateFormat)

    def prepare_post(self, post = None, request = None):
        if post == None:
            return
        post['date'] = post['date'].strftime(MainModel.globalDateFormat)
        post['updated'] = post['updated'].strftime(MainModel.globalDateFormat)
        post['url'] = request.route_url('post', post_url=post['url'])
        if request != None and 'img' in post and post['img'] != None:
            post['img'] = request.static_url('myimageboard_1:views/assets/img/content/' + post['img'])
        if request != None and 'user_logo' in post and post['user_logo'] != None:
            post['user_logo'] = request.static_url('myimageboard_1:views/assets/img/users/' + post['user_logo'])
    
    def catalog_posts(self, request = None, limit=10, offset=0, order="date", direction="DESC", search=None):
        getDisp = request.params.get('page', None)

        if getDisp != None:
            offset = int(getDisp) * limit

        query = self.build_catalog_query(limit, offset, order, direction, search)
        queryCnt = self.build_catalog_query(limit, offset, order, direction, search, True)
        posts = self.query_get(query)
        postsCnt = self.query_get_single(queryCnt)
        
        count = postsCnt['posts_count']
        
        for post in posts:
            self.prepare_post(post,request)
            
        pagination = self.prepare_pagination(request, count, limit, offset, order, direction, search)

        return {
            "list": posts,
            "all_count": count,
            "pagination": pagination
        }
        
    def prepare_pagination(self, request, count, limit, offset, order, direction, search):        
        pagination = []
        
        pagesCount = math.ceil(count/limit)
        currentIndex = math.ceil(offset/limit)
        
        indexStart = currentIndex - (self.pagination_disp+1) if currentIndex - (self.pagination_disp) > 0 else 0
        indexEnd = currentIndex + self.pagination_disp if currentIndex + self.pagination_disp < pagesCount else pagesCount-1
        
        for iter in range(indexStart+1, indexEnd+1):
            link = request.route_url('home')
            if iter > 1:
                link = request.route_url(
                        'home', _query={"page": iter} if search == None else {"page": iter, 'search': search}
                )
            pagination.append({
                "title": str(iter), 
                "link": link
            })
        
        return pagination;
    
    def build_catalog_query(self, limit=10, offset=0, order="date", direction="DESC", search=None, count = False, postUrl = None, noJoins=False):
        myT = self.tablename(PostsModel.table)
        uT = self.tablename(UsersModel.table)
        
        uTFields = ' * '
        
        if not noJoins:
            uTFields  = myT + ".*, "
            uTFields += uT + ".nickname as user_name, "
            uTFields += uT + ".id as user_id, "
            uTFields += uT + ".email as user_email, "
            uTFields += uT + ".logo as user_logo "

        query = ''
        
        if count:
            query += "SELECT count(*) as posts_count"
        else:
            query += "SELECT " + uTFields + " "
           
        if noJoins:
            query += " FROM " + myT  + " "
        else:
            query += """
                FROM """ + myT + """
                LEFT JOIN """ + uT + """
                    ON """ + myT + ".user = " + uT + """.id
            """
        if search != None or postUrl != None:
            query += " WHERE "
            
        if search != None:
            query += " title like '%" + search + "%'"
            
        if postUrl != None:
            if search != None:
                query += " AND "
            query += " url like '" + postUrl + "'"
        
        if order != None:
            query += " ORDER BY " + myT + "." + str(order) + " "
            if direction != None:
                query += direction
        
        if not count and limit != None:
            query += " LIMIT " + str(limit)
            
            if offset != None:
                query += " OFFSET " + str(offset)
                
        return query