import pandas as pd
import numpy as np
#from Util import yaml_load, my_timer,my_logger, Data_dir,write_list
import Util as U
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
#style.use('fivethirtyeight')



# Abstract data class
class Data(object):
    data = []
    dataframe = []

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

    def load(self):
        pass

    def save(self):
        pass

    def show_data(self):
        print self.data

    def show_dataframe(self):
        print self.Dataframe.head()

    def get_dataframe(self):
        return self.Dataframe

    def get_dataset(self):
        return self.Dataset

    def from_csv(self,path):
         self.Dataframe = pd.read_csv(path, engine='python', sep=";")
         self.Dataset = self.Dataframe.values



    def to_csv(self,path):
        self.dataframe.to_csv(path,sep=';')

    # split into train and test sets
    def split_data(self,percentage_training = 0.67):
        self.train_size = int(len(self.Dataset) * percentage_training)
        self.test_size = len(self.Dataset) - self.train_size
        self.train, self.test = self.Dataset[0:self.train_size, :], self.Dataset[self.train_size:len(self.Dataset), :]


class Timeseries(Data):


    dataX, dataY = [], []

    def __init__(self, dataframe):
        self.dataframe = dataframe
        data = self.dataframe.values
        data = data.astype('float32')
        self.data = data

    # Magic function call them by repr(MC)
    # Print all the necessary Info to recreate the object
    def __repr__(self):
        pass

    # Magic function call them by str(MC)
    # Print Info related to the object
    def __str__(self):
        pass

    '''
    convert an array of values into a dataset matrix
    X=t and Y=t+1

    Example of use:

    X, Y = create_dataset(dataset[1:10],1)

    trainX, trainY = create_dataset(train, look_back)
    testX, testY = create_dataset(test, look_back)

    '''
    # I am not sure If this is the right place (?)
    def create_labeled_dataset(self, look_back=1):

        for i in range(len(self.Dataset) - look_back - 1):
            a = self.Dataset[i:(i + look_back), 0]
            self.dataX.append(a)
            self.dataY.append(self.Dataset[i + look_back, 0])
        return np.array(self.dataX), np.array(self.dataY)

    # reshape input to be [samples, time steps, features]
    def reshape_dataset(self):
        self.trainX = np.reshape(self.trainX, (self.trainX.shape[0], 1, self.trainX.shape[1]))
        self.testX = np.reshape(self.testX, (self.testX.shape[0], 1, self.testX.shape[1]))

    def moving_average(self):
        pass

    # A class Method is used as a Second Constructor
    @classmethod
    def from_csv(cls, path):
        # Setting Up data and dataframe
        # Setting up index as time object
        dataframe = pd.read_csv(path, engine='python', index_col=[0], sep=";")
        dataframe.reset_index(drop=True)
        New_index = pd.to_datetime(dataframe.index)
        dataframe.index = New_index
        return cls(dataframe)


    # A static method is a method that doesn't access the instance or the class in the function
    @staticmethod
    def my_static_method():
        return True


    def to_csv(self,name,path=U.Data_dir):
        self.dataframe.to_csv(path+name, sep=";")
        

    def plot(self,title="No title", freq=None):
        if freq:
            self.dataframe.resample(freq).mean().plot()
        else:
            self.dataframe.plot()
        # Code Operational to plot with dates
        #plt.plot_date(self.dataframe.index, self.dataframe['cpu.idle_perc'], '--')
        plt.title(title)
        plt.show()

# TODO Create at least 3 SLOs for IMS Service
# TODO SLO Created by the manager ? !
class SLO(Data):

    data = None

    def __init__(self,path):
        #Yaml Reader
        self.data = U.yaml_load(path)

    def show(self):
        for item in self.data:
            print item.keys(), item.values()
            print "---"

    def get_values(self):
        return self.data
    # Magic function call them by repr(MC)
    # Print all the necessary Info to recreate the object
    def __repr__(self):
        pass

    # Magic function call them by str(MC)
    # Print Info related to the object
    def __str__(self):
        pass



class RawData(Data):

    # Use Json
    def __init__(self, path):
        with open(path) as data_file:
            self.data = json.load(data_file)


    def df_from_raw(self, group):
        i = 0
        raw = filter(None, self.data)
        log = 0;
        df = pd.DataFrame()
        #print('raw = {} '.format(raw))
        for s in raw:
            # print('s = {} '.format(s[0]))
            if s[0]['measurements'] and s[0]['dimensions']['hostname'] == group:
                m = np.array(s[0]['measurements'])
                timestamps = m[:, s[0]['columns'].index('timestamp')]
                df = pd.DataFrame(index=timestamps)
                break;
        m = 0;
        for measure in raw:
            if measure[0]['measurements'] and measure[0]['dimensions']['hostname'] == group:
                hostname = group
                m = np.array(measure[0]['measurements'])
                timestamps = m[:, measure[0]['columns'].index('timestamp')]
                # df = pd.DataFrame(index = timestamps)
                # getting name
                if (log == 1):
                    print 'metric : \n'
                    print measure[0]['name']
                name = measure[0]['name'];
                # getting dimensions
                if (log == 1):
                    print '\n Machine name : \n'
                    print measure[0]['dimensions']['hostname']
                # Getting measurement
                if (log == 1):
                    print '\n measurements \n'
                    print m  # measure[0]['measurements']

                # Measurement into Array

                m = np.array(measure[0]['measurements'])

                timestamps = m[:, measure[0]['columns'].index('timestamp')]
                if (log == 1):
                    print timestamps

                values = m[:, measure[0]['columns'].index('value')]
                if (log == 1):
                    print '\n values \n '
                    print values

                # vars()["df_"+str(i)] =  dict( zip( timestamps, m));

                df[name] = m[:, measure[0]['columns'].index('value')];

                if (log == 1):
                    print 'This is the dataframe' + 'is' + name

                # vars()["df_"+str(i)]['hostname'] = hostname;

                if (log == 1):
                    print ' \n \n ***********  --------------- *********** \n'
                i = i + 1;
        return df;

    @U.my_timer
    @U.my_logger
    def to_csv(self,host,path,metric={}):
        if metric:
            self.df_from_raw(host[metric]).to_csv(U.Data_dir+path, sep=";",index_label="Timestamp")
        else:
            self.df_from_raw(host).to_csv(U.Data_dir+path, sep=";",index_label="Timestamp")

if __name__ == '__main__':


    RD = RawData(U.Data_dir + "measurements.json")

    def measurements_to_csv():

        RD.to_csv('ellis.jaafar.com',"Ellis.csv")
        RD.to_csv('bono.jaafar.com', "Bono.csv")
        RD.to_csv('sprout.jaafar.com', "Sprout.csv")
        RD.to_csv('homer.jaafar.com', "Homer.csv")
        RD.to_csv('homestead.jaafar.com', "Homestead.csv")
        RD.to_csv('ralf.jaafar.com', "Ralf.csv")




    #U.write_list("Info.txt",RD.data[26])

    print type(RD.data[26][0]['measurements'])
    print len(RD.data[26][0]['measurements'])

    #TS =Timeseries()
    #New constructor
    # TS = Timeseries.from_csv(Data_dir+"test.csv")
    # print(help(TS))
    # TS.plot("title")





