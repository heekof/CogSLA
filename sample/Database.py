import sqlite3
import time
import datetime
import random
from Data import Timeseries
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#from Util import Data_dir,my_timer
import Util as U
from matplotlib import style
style.use('fivethirtyeight')

# TODO Implement also Influx or MangoDB
class Database(object):
    name = ''
    def __init__(self):
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

    # Magic function call them by repr(MC)
    # Print all the necessary Info to recreate the object
    def __repr__(self):
         pass

    # Magic function call them by str(MC)
    # Print Info related to the object
    def __str__(self):
        pass

    def connect(self):
        self.conn = sqlite3.connect(U.Data_dir+'timeseries.db')
        self.c = self.conn.cursor()


    # TODO automate the creation of the database
    def create_table(self, dataframe, name = "timeseries"):
        columns = dataframe.columns
        self.name = name
        champs = ''
        for c in columns:
            champs += ' '+c+' REAL'
            if not c == columns[-1]:
                champs += ', '

        champs = champs.translate(None, '.')
        #print champs
        self.c.execute('CREATE TABLE IF NOT EXISTS '+name+'(unix REAL, datestamp DATE, '+champs+' )')

    #@my_timer
    def write(self, dataframe):

        columns = dataframe.columns
        champs = ''
        point = ''
        for c in columns:
            point += "?"
            champs += " " + c
            if not c == columns[-1]:
                champs += ', '
                point += ","

        champs = champs.translate(None, '.')

        for i in range(len(dataframe)):

                #print i
            unix = time.mktime(datetime.datetime.strptime(str(dataframe.index[i]), "%Y-%m-%d %H:%M:%S.%f").timetuple())
            date = str(dataframe.index[i])
            values = []

            row_values = []
            for field in dataframe.columns:
                row_values.append(dataframe[field][i])
            values.append(row_values)
                #print values[0]

            #print("INSERT INTO "+self.name+" (unix, datestamp, "+champs+") VALUES (?,?,"+point+")",(unix,date,dataframe['net.out_packets_sec'][i],dataframe['cpu.idle_perc'][i],dataframe['cpu.stolen_perc'][i],dataframe['cpu.system_perc'][i],dataframe['cpu.wait_perc'][i],dataframe['disk.inode_used_perc'][i],dataframe['disk.space_used_perc'][i],dataframe['io.read_kbytes_sec'][i],dataframe['io.read_req_sec'][i],dataframe['io.read_time_sec'][i],dataframe['io.write_kbytes_sec'][i],dataframe['io.write_req_sec'][i],dataframe['io.write_time_sec'][i],dataframe['load.avg_15_min'][i],dataframe['load.avg_1_min'][i],dataframe['load.avg_5_min'][i],dataframe['mem.free_mb'][i],dataframe['mem.total_mb'][i],dataframe['mem.usable_perc'][i],dataframe['mem.usable_mb'][i],dataframe['net.in_bytes_sec'][i],dataframe['net.in_errors_sec'][i],dataframe['net.in_packets_dropped_sec'][i],dataframe['net.in_packets_sec'][i],dataframe['net.out_bytes_sec'][i],dataframe['net.out_errors_sec'][i]))
            self.c.execute("INSERT INTO "+self.name+" (unix, datestamp, "+champs+") VALUES (?,?,"+point+")",(unix,date,dataframe['net.out_packets_sec'][i],dataframe['cpu.idle_perc'][i],dataframe['cpu.stolen_perc'][i],dataframe['cpu.system_perc'][i],dataframe['cpu.wait_perc'][i],dataframe['disk.inode_used_perc'][i],dataframe['disk.space_used_perc'][i],dataframe['io.read_kbytes_sec'][i],dataframe['io.read_req_sec'][i],dataframe['io.read_time_sec'][i],dataframe['io.write_kbytes_sec'][i],dataframe['io.write_req_sec'][i],dataframe['io.write_time_sec'][i],dataframe['load.avg_15_min'][i],dataframe['load.avg_1_min'][i],dataframe['load.avg_5_min'][i],dataframe['mem.free_mb'][i],dataframe['mem.total_mb'][i],dataframe['mem.usable_perc'][i],dataframe['mem.usable_mb'][i],dataframe['net.in_bytes_sec'][i],dataframe['net.in_errors_sec'][i],dataframe['net.in_packets_dropped_sec'][i],dataframe['net.in_packets_sec'][i],dataframe['net.out_bytes_sec'][i],dataframe['net.out_errors_sec'][i]))


        self.conn.commit()


    def read_from_db(self):
        self.c.execute("SELECT * FROM Ellis")
        data = []
        for row in self.c.fetchall():
            #print row
            data.append(row)
        return data

    def plot(self,VNF,metric):

        metric = metric.translate(None, '.')
        self.c.execute("SELECT unix, "+metric+" FROM "+VNF+"")
        dates = []
        values = []
        pas = []
        i=0
        for row in self.c.fetchall():
            #print row
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


    @U.my_timer
    def send_to_database():



        # Second constructor
        TS_Ellis = Timeseries.from_csv("Ellis.csv")
        TS_Bono = Timeseries.from_csv("Bono.csv")
        TS_Sprout = Timeseries.from_csv("Sprout.csv")
        TS_Homer = Timeseries.from_csv("Homer.csv")
        TS_Homestead = Timeseries.from_csv("Homestead.csv")
        TS_Ralf = Timeseries.from_csv("Ralf.csv")


        MySQL.create_table(TS_Ellis.dataframe,"Ellis")
        MySQL.write(TS_Ellis.dataframe)

        MySQL.create_table(TS_Homer.dataframe, "Homer")
        MySQL.write(TS_Homer.dataframe)


        MySQL.create_table(TS_Homestead.dataframe, "Homestead")
        MySQL.write(TS_Homestead.dataframe)


        MySQL.create_table(TS_Ralf.dataframe, "Ralf")
        MySQL.write(TS_Ralf.dataframe)

        MySQL.create_table(TS_Sprout.dataframe, "Sprout")
        MySQL.write(TS_Sprout.dataframe)


        MySQL.create_table(TS_Bono.dataframe, "Bono")
        MySQL.write(TS_Bono.dataframe)


    '''
    Read from SQL

    '''

    #print 'The length of the data is '.format(len(MySQL.read_from_db()))

    def plot():
        MySQL.plot("Bono","cpu.idle_perc")

    #@my_timer
    send_to_database()

    MySQL.c.close()
    MySQL.conn.close()

