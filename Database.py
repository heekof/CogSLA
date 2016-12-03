


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

