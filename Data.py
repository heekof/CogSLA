import pandas as pd
import numpy as np

# Abstract data class
class Data(object):
    Dataset = None
    Dataframe = None
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
        print self.Dataset

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
        self.Dataset.to_csv(path,sep=';')

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








class SLO(Data):

    def read_slo(self):
        pass

    def write_slo(self):
        pass


