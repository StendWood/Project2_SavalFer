# coding: utf-8

# Imports
import pygame
import psycopg2
import hashlib
import os

# Additional code
from game.config import *


class Database:
    """
        Database hub
    """

    def __init__(self, login=None):
        self.host = HOST
        self.database = DATABASE
        self.user = USER
        self.password = PASSWORD
        self.login = login

    def connection(self):
        """
            Create a connection to the database
        """

        self.conn = psycopg2.connect(
                        host=self.host,
                        database=self.database,
                        user=self.user,
                        password=self.password
                        )


    def manage_cursor(self, flag=0):
        """
            Create a connection cursor if flag = 1 | close the cursor if flag = 0
        """

        if flag == 1:
            print("Creating cursor...\n")
            self.cur = self.conn.cursor()
        else:
            print("Cursor closed\n")
            self.cur.close()


    def close_conn(self):
        """
            Close the connection to the server | MUST BE DONE. ALWAYS.
        """

        # Close the communication with the PostgreSQL
        print(f"\nConnection to {HOST} closed.")
        self.conn.close()


    def global_query(self, query):
        # Create the connection
        self.connection()
        # Create the cursor
        self.manage_cursor(1)
        # Execute the Query
        self.cur.execute(query)
        # Fetch the results
        query_result = self.cur.fetchall()
        # Commit the insert to the db
        if "insert" in query:
            self.conn.commit()
        # Close the cursor
        self.manage_cursor()
        # Close connection
        self.conn.close()
        return query_result

    def insert_query(self, table_name: str, rows_name: str, data_to_insert: str):
        """
            Insert into the database | rows_name = "row_1, row_2, etc..." | data_to_insert = (data_1, data_2, etc...)
        """

        # Create a cursor
        self.manage_cursor(1)
        # Query
        query = f"""
                        INSERT INTO {table_name} ({rows_name}) VALUES ({data_to_insert});
                        """
        # Insert Query
        self.cur.execute(query)
        # Commit the insert to the db
        self.conn.commit()
        # Close the cursor
        self.manage_cursor()


    def password_checker(self, username: str, password: str):
        """
            Check if the credentials are a valid by comparing to the DB
        """

        self.conn = None
        try:
            # Connect to the database
            self.connection()
            # Create a cursor
            self.manage_cursor(1)

            # INSERT into the DB
            query = f"""
                            SELECT password, salt FROM "{DB_PREFIX}".login
                            WHERE username = '{username}';
                        """
            # Insert Query
            self.cur.execute(query)
            # Get back credentials from the DB
            credentials = self.cur.fetchone()
            # Cursor closed
            self.manage_cursor()
            # Transform DB password and DB salt back to bytes
            db_pwd = bytes(credentials[0])
            db_salt = bytes(credentials[1])
            # Hash the entered password using the DB salt
            pwd_to_check = self.hashing(password, db_salt)
            # Check if both password are a match
            if pwd_to_check == db_pwd:
                # Set login flag to false to launch the game
                self.login.game.login_flag = False
                # Save the username if necessary
                if self.login.game.cfg["save_username"]:
                    self.login.game.cfg["username_text"] = self.login.username_text
                # Stop the music
                pygame.mixer.music.fadeout(3000)
                # Delete the login object to free memory
                del(self.login)
            else:
                # Set error to true to show the error popup
                self.login.login_error = True

        except TypeError:
            # Set error to true to show the error popup
            self.login.login_error = True

        # Error catching during connection or queries
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            # If a connection is established - close the cursor and the connection
            if self.conn is not None:
                self.close_conn()


###########
# HASHING #
###########

    def random_hashing(self, input_data: str):
        """
            Hash the user inputed password after generating a random salt
        """

        # Randomize a salt
        salt = os.urandom(32)
        print("\nSALT : ", salt)
        print(len(salt))
        print()
        # Hash the password
        input_data = hashlib.pbkdf2_hmac('sha256', input_data.encode('utf-8'), salt, 100000)
        print("Hash : ", input_data)
        print(len(input_data))

        # Return the salt and the hashed password
        return salt, input_data


    def hashing(self, pwd: str, salt: bytes):
        """
            Hash the user inputed password using the DB salt
        """
        print()
        print(pwd)
        print()
        print(salt)
        # Hash the password
        pwd = hashlib.pbkdf2_hmac('sha256', pwd.encode('utf-8'), salt, 100000)
        # Return the hashed password
        return pwd
