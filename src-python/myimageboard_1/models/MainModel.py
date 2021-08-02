import mysql
from mysql.connector import connect, Error

class MainModel:

    connection = None
    globalDateFormat = '%Y.%m.%d %H:%M:%S'

    tablePrefix = 'myimageboard_1_'
    
    dumpQueries = False

    def __init__(self):
        self.connect_mysql_connector_python()
            
    def tablename (self, name):
        return self.tablePrefix + name
        
    def is_connected(self):
        return MainModel.connection != None and MainModel.connection.is_connected()
    
    def query(self, execQuery):
        if self.dumpQueries: 
            print(execQuery)
        
        if not self.is_connected():
            print("No DB connection available")
            return None        
        
        try:
            cursor = MainModel.connection.cursor()
            cursor.execute(execQuery)
        except mysql.connector.Error as err:
            print("Failed query: {}".format(err))
            return False
            
        cursor.close()
        return True
        
    def query_get(self, query):
        if self.dumpQueries: 
            print(query)
        
        if not self.is_connected():
            print("No DB connection available")
            return None
            
        try:
            cursor = MainModel.connection.cursor(dictionary=True)
            cursor.execute(query)
        except mysql.connector.Error as err:
            print("Failed query: {}".format(err))
            return None
            
        aggr = []

        for row in cursor:
            aggr.append(row)
        
        cursor.close()
        return aggr
        
    def query_get_single(self, query):
        if self.dumpQueries: 
            print(query)
        
        if not self.is_connected():
            print("No DB connection available")
            return None
            
        try:
            cursor = MainModel.connection.cursor(dictionary=True)
            cursor.execute(query)
        except mysql.connector.Error as err:
            print("Failed query: {}".format(err))
            return None
        

        for row in cursor:
            cursor.close()
            return row
        
        cursor.close()        
        return None
        
    def connect_mysql_connector_python(self):
        if self.is_connected():
            return 

        try:
            MainModel.connection = connect(
                host="localhost",
                user='myimageboard_1',
                password='myimageboard_1',
                database='myimageboard_1',
                use_pure=False
            )                 
        except Error as e:
            print("ERROR: " + e)
            return

        if self.is_connected():
            if self.dumpQueries: 
                print('CONNECTED:')
                print(self.connection)
        else:
            print('NO CONNECTION!!!')