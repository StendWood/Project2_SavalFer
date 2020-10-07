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

        self.host = "localhost"
        self.database = "p2"
        self.user = "postgres"
        self.password = "Formation2020-at"


    def db_connect(self):
        """
            Create a connection to the database
        """
        self.connection = psycopg2.connect(
                        host=self.host,
                        database=self.database,
                        user=self.user,
                        password=self.password
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






        

