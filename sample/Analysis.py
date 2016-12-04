#  Scikit-Learn
from sklearn import linear_model
from sklearn.preprocessing import MinMaxScaler
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
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

if __name__ == "__main__":
    #
    # Diabetes Dataset

    diabetes = datasets.load_diabetes()
    diabetes_X_train = diabetes.data[:-20]
    diabetes_X_test = diabetes.data[-20:]
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]

    #
    regr = linear_model.LinearRegression()
    regr.fit(diabetes_X_train, diabetes_y_train)
    linear_model.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    print(regr.coef_)
    # The mean square error
    print np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2)

    # Explained variance score: 1 is perfect prediction
    # and 0 means that there is no linear relationship
    # between X and y.
    print regr.score(diabetes_X_test, diabetes_y_test)

    # print diabetes_X_test, diabetes_y_test

    # plt.plot(diabetes_X_test,diabetes_y_test)
    # plt.show()