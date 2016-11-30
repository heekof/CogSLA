
from Data import Data
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

class Visualization(object):
    Data = None


    def __init__(self,Data):
        self.Data = Data

    def read(self):
        pass

    def save(self,plt,name,path="Figures/"):
        # see how to write it ...
        plt.savefig(path+name)


    def show(self):
        pass


class GraphViz(Visualization):

    def showgraph(self,plt):
        # show graph
        self.Data.Dataframe.plot()
        self.plt = plt
        plt.show()


    def showgraph_by_name(self,plt,name,start=0,end=100):
        # show graph
        self.Data.Dataframe[name][start:end].plot()
        self.plt = plt
        plt.show()


class TableViz(Visualization):
    pass

'''
MyData = Data()
MyData.load()
# print as a text
MyData.show_data()
G = GraphViz(MyData)
G.show()
G.showgraph(plt)
'''