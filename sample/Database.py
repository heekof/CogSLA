import sqlite3
import time
import datetime
import random


# TODO Implement SQL and Influx or MangoDB
class Database(object):
    pass


class MangoDB(Database):

    URI = "mongodb://127.0.0.1:27017"
    SQL = "localhost"
    database = None

    def __init__(self):
        pass  # This method now doesn't do anything. We could just delete it.

    @staticmethod
    def connect(self):
        # This initialises the connection to the URI
        # client = pymongo.MongoClient(Database.URI)
        #  This creates a variable which is the 'fullstack' database in that connection
        database = client['fullstack']

    def find(collection, query):
        return Database.database[collection].find(query)

    def find_one(collection, query):
        return Database.database[collection].find_one(query)

    def insert(collection, data):
        return Database.database[collection].insert(data)


class SQL(Database):
    c = None
    conn = None
    def __init__(self):
        pass

    def connect(self):
        self.conn = sqlite3.connect('Data/tutorial.db')
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

    def data_entry(self):
        self.c.execute("INSERT INTO stuffToPlot VALUES(45654564,'2016-01-01','Python','5')")
        self.conn.commit()
        self.c.close()
        self.conn.close()


if __name__ == "__main__":
    MySQL = SQL()
    MySQL.connect()
    MySQL.create_table()
    MySQL.data_entry()

