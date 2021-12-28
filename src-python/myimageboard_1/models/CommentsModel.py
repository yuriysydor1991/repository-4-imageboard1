from .MainModel import MainModel
from .UsersModel import UsersModel

class CommentsModel(MainModel):
    table = "comments"
    
    def __init__(self):
      super().__init__ () ;

    def all(self):
        cT = self.tablename(CommentsModel.table)
        query = "SELECT * FROM " + cT + " ORDER BY date DESC;"
        
        comments = self.query_get(query)
        
        for comment in comments:
            self.prepare_comment_dates(comment)
            
        return comments
        
    def allReactAdmin(self, request, count=False):
        start = int(request.params.get('_start', 0))
        end = int(request.params.get('_end', 10))
        order = request.params.get('_sort', 'date')
        limit = end - start
        offset = start
        direction = request.params.get('_order', 'desc')
        
        query = self.buildQueryReact(limit, offset, order, direction, count)
        
        if count:
            dbr = self.query_get_single(query)
            cnt = dbr["comments_count"]
            return cnt
        
        comments = self.query_get(query)
        
        for comment in comments:
            self.prepare_comment_dates(comment)
            
        return comments
        
    def prepare_comment_dates(self, comment):
        comment['date'] = comment['date'].strftime(MainModel.globalDateFormat)
        comment['updated'] = comment['updated'].strftime(MainModel.globalDateFormat)
        
    def buildQueryReact (self, limit=10, offset=0, order='date', direction="desc", count=False):
        myT = self.tablename(CommentsModel.table)
        
        uTFields = ' * '

        query = ''
        
        if count:
            query += "SELECT count(*) as comments_count"
        else:
            query += "SELECT " + uTFields + " "
           
        query += " FROM " + myT  + " "
        
        if order != None:
            query += " ORDER BY " + myT + "." + str(order) + " "
            if direction != None:
                query += direction
        
        if not count and limit != None:
            query += " LIMIT " + str(limit)
            
            if offset != None:
                query += " OFFSET " + str(offset)
                
        return query
   
    def allByPost(self, postId, request, count = False):
        cT = self.tablename(CommentsModel.table)
        uT = self.tablename(UsersModel.table)

        Fields  = cT + ".*, " 
        Fields += uT + ".nickname as user_nickname, "
        Fields += uT + ".email as user_email, "
        Fields += uT + ".id as user_id, "
        Fields += uT + ".logo as user_logo "

        if count:
            Fields = ' count(*) as comments_count'

        query = """
                    SELECT 
                        """ + Fields + """ 
                    FROM 
                        """ + cT + """
                        LEFT JOIN """ + uT + " ON " + uT + ".id = " + cT + ".user" + """
                    WHERE
                        """ + cT + ".post = " + str(postId) + """
                    ORDER BY """ + cT + """.date ASC
                    ;
        """

        if count:
            return self.query_get_single(query);

        comments = self.query_get(query);

        if comments == None:
            return None

        for comment in comments:
            if request != None and 'user_logo' in comment and comment['user_logo'] != None:
                comment['user_logo'] = request.static_url('myimageboard_1:views/assets/img/users/' + comment['user_logo'])

            comment['date'] = comment['date'].strftime(MainModel.globalDateFormat)
            comment['updated'] = comment['updated'].strftime(MainModel.globalDateFormat)

        return comments
