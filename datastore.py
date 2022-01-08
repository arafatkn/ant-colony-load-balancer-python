import mysql.connector
import os


class Datastore:
    db = None

    @staticmethod
    def make_ready():
        if os.path.exists("data/storage.db"):
            os.remove("data/storage.db")

        Datastore.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ant_colony"
        )


