from .MainModel import MainModel
from .CommentsModel import CommentsModel
from .UsersModel import UsersModel
from .PostsModel import PostsModel

class InitModel(MainModel):

    def __init__(self):
        super().__init__()

    def initBD(self):
        self.initUsers()
        self.initPosts()
        self.initComments()
        
    def initUsers(self):
        tName = self.tablename(UsersModel.table)
        self.dropTable(tName)
        self.query(
            """
                create table """ + tName + """
                (
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    nickname VARCHAR(128) DEFAULT NULL,
                    password VARCHAR(128) DEFAULT NULL,
                    email VARCHAR(128) DEFAULT NULL,
                    logo VARCHAR(1024) DEFAULT NULL,
                    website VARCHAR(128) DEFAULT NULL,
                    date TIMESTAMP DEFAULT current_timestamp(),
                    updated TIMESTAMP DEFAULT current_timestamp() ON UPDATE current_timestamp()
                );
            """
        )
        
        self.query("""
            INSERT INTO """ + tName + """
            (nickname, password, email)
            VALUES
            ('cc', 'cc', 'yuriysydor1991@gmail.com')
        """)
        
        self.query("""
            INSERT INTO """ + tName + """
            (nickname, password, email)
            VALUES
            ('cc2', 'ccnhs;jahwtehj5eoglndbkltseyo5', '2-yuriysydor1991@gmail.com')
        """)
        
        self.query("""
            INSERT INTO """ + tName + """
            (nickname, password, email)
            VALUES
            ('cc3', 'ccnhs;jahwtehj5eoglndbkltseyo5', '3-yuriysydor1991@gmail.com')
        """)

    def initComments(self):
        tName = self.tablename(CommentsModel.table)
        self.dropTable(tName)
        self.query(
            """
                create table """ + tName + """
                (
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    post INT DEFAULT NULL,
                    user INT DEFAULT NULL,
                    comment TEXT,
                    date TIMESTAMP DEFAULT current_timestamp(),
                    updated TIMESTAMP DEFAULT current_timestamp() ON UPDATE current_timestamp()
                );
            """
        )
        
        self.query("insert into myimageboard_1_comments (post, user, comment) VALUES (125, 1, 'Valid comment.');")
        self.query("insert into myimageboard_1_comments (post, user, comment) VALUES (125, 1, 'Another valid comment.');")
        self.query("insert into myimageboard_1_comments (post, user, comment) VALUES (125, 1, 'Criticising comment.');")
        
        for iter in range(1, 100):
            self.query("insert into myimageboard_1_comments (post, user, comment) VALUES (125, 1, 'Post comment #" + str(iter) + "');")
        
    def initPosts(self):
        tName = self.tablename(PostsModel.table)
        self.dropTable(tName)
        self.query(
            """
                create table """ + tName + """
                (
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    user INT DEFAULT NULL,
                    type VARCHAR(128) DEFAULT 'image-regular',
                    title VARCHAR(128) DEFAULT NULL,
                    url VARCHAR(128) DEFAULT NULL,
                    img VARCHAR(1024) DEFAULT NULL,
                    meta_keywords VARCHAR(1024) DEFAULT NULL,
                    meta_description VARCHAR(1024) DEFAULT NULL,
                    views INT DEFAULT 0,
                    date TIMESTAMP DEFAULT current_timestamp(),
                    updated TIMESTAMP DEFAULT current_timestamp() ON UPDATE current_timestamp(),
                    UNIQUE (url)
                );
            """
        )
        
        for i in range(1, 123):
            self.query("""
            INSERT INTO """ + tName + """
            (user, title, url, img)
            VALUES
            ('1', 'Heart of pluto """ + str(i) + """', 'heart-of-pluto-""" + str(i) + """', 'pluto-heart.jpg')
        """)
        
        self.query("""
            INSERT INTO """ + tName + """
            (user, title, url, img)
            VALUES
            ('1', 'Earth behind Moon rocks view', 'earth-behind-Moon-rocks-view', 'earth-moon-view.jpg')
        """)
        
        self.query("""
            INSERT INTO """ + tName + """
            (user, title, url, img)
            VALUES
            ('1', 'Mars Olimp space sideview', 'mars-olimp-space-sideview', 'mars-olimp.jpg')
        """)
        
        self.query("""
            INSERT INTO """ + tName + """
            (user, title, url, img)
            VALUES
            ('1', 'Heart of pluto', 'heart-of-pluto', 'pluto-heart.jpg')
        """)
    
    def dropTable(self, tableName):
        self.query("DROP TABLE " + tableName + ";")
        