from .MainModel import MainModel

class UsersModel(MainModel):
    table = "users"
    User = None
    
    def __init__(self):
        self.user = None
    
    def cleanedUser(self):
        if (self.signed()):
            return {
                    'id': UsersModel.User['id'],
                    'nick': UsersModel.User['nickname'],
                    'email': UsersModel.User['email'],
                    'logo': UsersModel.User['logo'],
                    'website': UsersModel.User['website'],
            }
        else:
            return None
    
    def signed(self):
        return UsersModel.User != None and "id" in UsersModel.User;
        
    def signin(self, userId):
        UsersModel.User = self.get(userId)
    
    def getByUserPass(self, nickname, password):
        if len(nickname) == 0 or len(password) == 0 :
            return {}
            
        return self.query_get_single(
                "SELECT * FROM " 
                + self.tablename(UsersModel.table)
                + " WHERE "
                + "nickname = '" + nickname + "'"
                + " AND "
                + "password = '" + password + "'"
                + ";"
        );
    
    def get(self, id):
        return self.query_get_single(
                "SELECT * FROM "
                + self.tablename(UsersModel.table)
                + " WHERE id = " + str(id) + ";"
            )
            
    def all(self):
        rows = self.query_get(
                    "SELECT * FROM " 
                    + self.tablename(UsersModel.table) 
                    + ";"
                )
                
        for user in rows:
            self.prepare_user_row(user)
            
        return rows
    
    def prepare_user_row(self, user):
        user['date'] = user['date'].strftime(MainModel.globalDateFormat)
        user['updated'] = user['updated'].strftime(MainModel.globalDateFormat)