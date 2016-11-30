import pandas as pd
import matplotlib.pyplot as plt
'''

Local imports

'''
from Data import Timeseries,SLO
from Analysis import Analysis,Result
from Visualization import GraphViz
from Database import MonascaConnect
from Util import initLog


logger = initLog('log/system.log',debug=1)
logger.debug("Start of the Main Program")

TS = Timeseries()
TS.from_csv("Data/sprout.csv")
#print TS.get_dataframe()
Graph = GraphViz(TS)
dataframe = pd.DataFrame()
dataframe = Graph.Data.Dataframe
dataframe.plot()

plt.plot([1,2,3])


#MC = MonascaConnect()
#MC.authenticate()
#check error here
#MC.request()
#MC.show_measurements()
