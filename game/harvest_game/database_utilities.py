# coding: utf-8

# import module
import psycopg2

class Database():
    """
        manages the connection to the database "P2"
    """

    def __init__(self):
        """
            constructor
        """

        self.host = "ale-pyt-2006-pjt-p2-db.pythonrover.wilders.dev"
        self.database = "postgres"
        self.dbname = "SavalFer"
        self.user = "AP2006"
        self.password = "AP2006p2"
        self.port = "15002"


    def db_connect(self):
        """
            Create a connection to the database
        """
        self.connection = psycopg2.connect(
                        host=self.host,
                        dbname = self.dbname,
                        user=self.user,
                        password=self.password,
                        port = self.port
                        )
    

    def execute_query(self, current_query, needed_result = False):
        """
            Execute specified query
        """
        
        self.db_connect()

        self.cursor = self.connection.cursor()
        self.cursor.execute(current_query)

        if needed_result:
            self.result = self.cursor.fetchall()
            return self.result
        else:
            self.connection.commit()

        self.cursor.close()






        

