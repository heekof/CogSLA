
import matplotlib.pyplot as plt


class Visualization(object):
    data = None
    plt = plt


    def __init__(self, data, plt):
        self.data = data
        self.plt = plt

        # Magic function call them by repr(MC)
        # Print all the necessary Info to recreate the object
    def __repr__(self):
         pass

    # Magic function call them by str(MC)
    # Print Info related to the object
    def __str__(self):
         pass

    def read(self):
        pass

    def save(self, name, path="Figures/"):
        # see how to write it ...
        self.data.dataframe.plot()
        self.plt.savefig(path+name)

    def show(self):
        pass


class GraphViz(Visualization):

    def show_graph(self):
        # show graph
        self.data.dataframe.plot()
        self.plt.show()

    def animated_graph(self):
        pass

    def showgraph_by_name(self,plt,name,start=0,end=100):
        # show graph
        self.data.dataframe[name][start:end].plot()
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