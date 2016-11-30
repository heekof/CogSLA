
from Data import Data
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

class Visualization(object):
    Data = Data()

    def __init__(self,Data):
        self.Data = Data

    def read(self):
        pass

    def save(self,path="Figures"):
        # see how to write it ...
        self.show()


    def show(self):
        pass


class GraphViz(Visualization):

    def showgraph(self):
        # show graph
        pass

class TableViz(Visualization):
    pass


MyData = Data()
MyData.load()
# print as a text
MyData.show_data()
G = GraphViz(MyData)
G.show()
G.showgraph()
