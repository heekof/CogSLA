import pandas as pd
import numpy as np
from Util import yaml_load, read_list
import json
import matplotlib.pyplot as plt
# Abstract data class
class Data(object):
    data = []
    dataframe = []
    train_size = None
    test_size = None
    train = None
    test = None


    def __init__(self):
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

    def __init__(self):
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

    def from_csv(self, path):
        # Setting Up data and dataframe
        # Setting up index as time object
        self.dataframe = pd.read_csv(path, engine='python', index_col=[0], sep=";")
        self.dataframe.reset_index(drop=True)
        New_index = pd.to_datetime(self.dataframe.index)
        self.dataframe.index = New_index
        self.data = self.dataframe.values
        self.data = self.data.astype('float32')

    def to_csv(self,name,path="sample/Data/"):
        self.dataframe.to_csv(path+name, sep=";")

    def plot(self,title="No title", freq=None):
        if freq:
            self.dataframe.resample(freq).mean().plot()
        else:
            self.dataframe.plot()
        plt.title(title)
        plt.show()

# TODO Create at least 3 SLOs for IMS Service
class SLO(Data):

    data = None

    def __init__(self,path):
        #Yaml Reader
        self.data = yaml_load(path)

    def show(self):
        for item in self.data:
            print item.keys(), item.values()
            print "---"

    def get_values(self):
        return self.data


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

    def to_csv(self,host,path,metric={}):
        if metric:
            self.df_from_raw(host[metric]).to_csv("sample/Data/"+path, sep=";")
        else:
            self.df_from_raw(host).to_csv("sample/Data/"+path, sep=";")

if __name__ == '__main__':

    RD = RawData("sample/Data/measurements.json")
    RD.to_csv('ellis.jaafar.com',"test.csv")

    TS =Timeseries()
    TS.from_csv("sample/Data/test.csv")
    TS.plot("title")





