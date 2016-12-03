import sqlite3
import time
import datetime
import random
from Data import Timeseries
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

# TODO Implement also Influx or MangoDB
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
        self.conn = sqlite3.connect('sample/Data/timeseries.db')
        self.c = self.conn.cursor()


    # TODO automate the creation of the database
    def create_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS Ellis(unix REAL, datestamp TEXT, value REAL)')

    def write(self, dataframe):

        #date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        for i in range(len(dataframe)):
            #date = datetime.datetime.strftime(dataframe.index[i],'%Y-%m-%d %H:%M:%S.%f')
            #print i
            #print dataframe.index[i]
            if i != 241:
                unix = time.mktime(datetime.datetime.strptime(str(dataframe.index[i]), "%Y-%m-%d %H:%M:%S.%f").timetuple())
                date = str(dataframe.index[i])
                value = dataframe['cpu.idle_perc'][i]
                #print "date {} and value {} ".format(date,value)
                self.c.execute("INSERT INTO Ellis (unix, datestamp, value) VALUES (?,?,?)",
                           (unix, date, value))

        self.conn.commit()


    def read_from_db(self):
        self.c.execute("SELECT * FROM Ellis")
        data = []
        for row in self.c.fetchall():
            #print row
            data.append(row)
        return data

    def plot(self):
        self.c.execute("SELECT unix,value FROM Ellis")
        dates = []
        values = []
        pas = []
        i=0
        for row in self.c.fetchall():
            print row
            #print i
            dates.append(datetime.datetime.fromtimestamp(row[0]))
            values.append(row[1])
            pas.append(i)
            i += 1

        plt.plot_date(dates[1:100], values[1:100], '--')
        #plt.scatter(pas[1:100], values[1:100])
        plt.show()


if __name__ == "__main__":
    '''
    Write TS to SQL

    '''
    MySQL = SQL()
    MySQL.connect()
    MySQL.create_table()

    TS = Timeseries()
    TS.from_csv("sample/Data/test.csv")

    MySQL.write(TS.dataframe)
    #MySQL.c.close()
     #MySQL.conn.close()

    '''
    Read from SQL

    '''

    #print 'The length of the data is '.format(len(MySQL.read_from_db()))
    MySQL.plot()

    MySQL.c.close()
    MySQL.conn.close()

