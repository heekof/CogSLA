import pandas as pd
import matplotlib.pyplot as plt
'''

Local imports

'''
from Data import Timeseries,SLO
from Analysis import Analysis,Result
from Visualization import GraphViz
from Database import MonascaConnect
from Util import initLog,write_list


logger = initLog('log/system.log',debug=1)
logger.debug("Start of the Main Program")

if __name__ == '__main__' and False:

    # Create the Data Class
    TS = Timeseries()
    # Import Data
    TS.from_csv("Data/sprout.csv")
    # Create Viz Object with Data as TS
    Graph = GraphViz(TS)
    # plot the Data
    Graph.showgraph_by_name(plt,'cpu_wait_perc',10,50)
    Graph.save(plt,'maFigure.png')








MC = MonascaConnect()
MC.authenticate()
#resp = MC.monasca_client.metrics.list()
#print type(resp)
#write_list("Data/response_monasca.txt",resp)

#check error here
#MC.request()
#MC.show_measurements()
