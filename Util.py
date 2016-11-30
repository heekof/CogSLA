import datetime
import time
# Import libraries use for visualization and analysis
import pandas as pd
import numpy as np
#import cufflinks as cf




OS_PROJECT_NAME='mini-mon'
password='password'
OS_AUTH_URL='http://157.159.232.218:35357/v3/'
username='mini-mon'
MONASCA_API_URL='http://157.159.232.217:8070/v2.0/'
monasca_url = 'http://157.159.232.217:8070/v2.0/'

keystone_url = 'http://157.159.232.218:35357/v3/'
api_version = '2_0'








def Timestamp(df):
    tsp = np.array(df.index)
    i=0;
    for ind in tsp:
        tsp[i] = time.mktime(datetime.datetime.strptime(repr(str(ind))[1:-1], '%Y-%m-%dT%H:%M:%S.%fZ').timetuple())
        i += 1;
    return tsp


def stamped_df(dframe):

    dframe['Timestamp']=Timestamp(dframe)
    dframe.index.names = [None]
    dframe = dframe.reset_index(drop=True)
    dframe = dframe.set_index('Timestamp')


    return dframe

