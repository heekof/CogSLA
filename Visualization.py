
from Data import Data


class Visualization(object):

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
        self.Data

class TableViz(Visualization):
    pass


MyData = Data()
MyData.load()
# print as a text
MyData.show_data()
G = GraphViz(MyData)
G.show()
G.showgraph()
