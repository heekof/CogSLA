#  Scikit-Learn
from sklearn.preprocessing import MinMaxScaler
from Data import Data

class Analysis(object):
    Data = None

    def __init__(self,Data):
        self.Data = Data

    def process(self):
        pass

    def normalization(self,min,max):
        # normalize the dataset thanks to scikit-learn
        scaler = MinMaxScaler(feature_range=(min, max))
        self.Data.Dataset = scaler.fit_transform(self.Data.get_dataset())


class PCA(Analysis):
    pass

class Pearson(Analysis):
    pass

class Autocorrelation(Analysis):
    pass



class Result:
    pass