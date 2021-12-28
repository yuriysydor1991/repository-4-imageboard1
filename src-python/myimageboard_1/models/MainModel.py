import mysql
from mysql.connector import connect, Error

class MainModel:

    connection = None
    globalDateFormat = '%Y.%m.%d %H:%M:%S'

    tablePrefix = 'myimageboard_1_'
    
    dumpQueries = True

    def __init__(self):
        self.connect_mysql_connector_python()
            
    def tablename (self, name):
        return self.tablePrefix + name
        
    def is_connected(self):
        if self.dumpQueries:
            print("is_connected() : connection present: " + str(self.connection != None))
            if self.connection != None:
                print("is_connected() : connection.is_connected(): " + str(self.connection.is_connected()))
            
        return self.connection != None and self.connection.is_connected()
    
    def query(self, execQuery):
        if self.dumpQueries:
            print(execQuery)
        
        if not self.is_connected():
            print("query() : No DB connection available")
            return None
        
        try:
            cursor = self.connection.cursor()
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
            print("query_get() : No DB connection available")
            return None
            
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
        except mysql.connector.Error as err:
            print("query_get() : Failed query: {}".format(err))
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
            print("query_get_single() : No DB connection available")
            return None
            
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
        except mysql.connector.Error as err:
            print("query_get_single() : Failed query: {}".format(err))
            return None
        

        for row in cursor:
            cursor.close()
            return row
        
        cursor.close()        
        return None
        
    def connect_mysql_connector_python(self):
        print ("connect_mysql_connector_python() : checking")
        if self.is_connected():
            print ("connect_mysql_connector_python() : connected")
            return 

        print ("connect_mysql_connector_python() : not connected, trying")
        
        try:
            self.connection = connect(
                host="localhost",
                user='myimageboard_1',
                password='myimageboard_1',
                database='myimageboard_1',
                use_pure=True,
                autocommit=True
            )                 
        except Error as e:
            print("connect_mysql_connector_python() : Failed query: {}".format(e))
            return

        if self.is_connected():
            if self.dumpQueries: 
                print('connect_mysql_connector_python() : CONNECTED:')
                print(self.connection)
        else:
            print('connect_mysql_connector_python() : NO CONNECTION!!!')
