import pandas as pd
import matplotlib.pyplot as plt
'''

Local imports

'''
from Service import Service,SLA
from Data import Timeseries,SLO
from Analysis import Analysis,Result
from Visualization import GraphViz
from Monasca import Monasca
from Util import initLog,write_list,read_file


logger = initLog('log/system.log',debug=1)
logger.debug("Start of the Main Program")

if __name__ == '__main__':
    pass

# TODO This is a to do comment


'''
Working with Time Series

# Create the Data Class
TS = Timeseries()
# Import Data
TS.from_csv("Data/net_out_demo_1_min.csv")
# print TS.dataframe.head(5)
# print TS.data[10:20]
'''


'''
Working with Graphs


# Create Viz Object with Data as TS
# Create the Graph
Graph = GraphViz(TS, plt)
# plot the Data
Graph.show_graph()
Graph.save("maFigure.png")

'''




'''
    Working with SLA and SLOs
    We should define 2 SLOs based on IMS Service


SLO_response_time = SLO("SLA/SLO/service-name-slo.yaml")

# print 'SLO key 2= {} '.format(SLO_response_time.get_values()[2].keys())
# print 'SLO key 3= {} '.format(SLO_response_time.get_values()[2].values())


MySLA = SLA(SLO_response_time)
IMS_Service = Service(MySLA,"Description of service")

print IMS_Service.SLA.SLO.get_values(),

'''



