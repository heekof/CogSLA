import datetime
import time
from monascaclient import client
from monascaclient import ksclient
import pandas as pd
import numpy as np
#from Util import ALL, Data_dir
import Util as U
from Password import *
import json
import pickle

class Monasca:

    database = None
    ks = None
    monasca_client = []
    metrics = []
    measurements = []


    def __init__(self):
       #  self.measurements = read_list("Data/Measurements.txt")
        pass
    # TODO: Implement Magic functions
    # Magic function call them by repr(MC)
    # Print all the necessary Info to recreate the object
    def __repr__(self):
        pass

    # Magic function call them by str(MC)
    # Print Info related to the object
    def __str__(self):
        pass

    #@staticmethod
    def authenticate(self):

        # Authenticate to Keystone
        try:
            # connecting
            self.ks = ksclient.KSClient(auth_url=KEYSTONE_URL, username=USERNAME, password=PASSWORD)
            # construct the mon client
            self.monasca_client = client.Client(api_version, MONASCA_URL, token=self.ks.token)
        except:
             print('Connection error !')
        else:
            print('Connected to monasca server !')

    def get_monasca_client(self):
        return self.monasca_client

    def request(self, start_time, end_time, metrics=['net.out_packets_sec'],dimensions={}):
        self.metrics = metrics

        # The error was HEre self.metrics instead of metrics
        self.measurements = self.get_measurements(self.get_metrics(metrics,dimensions,limit={}), start_time, end_time)

    def show_measurements(self):
        print self.measurements

    # getting the metrics information
    def get_metrics(self, names=[None], dimensions={}, limit={}):
        metrics = []
        for name in names:
            # Invoke the Monasca client
            metrics = metrics + self.monasca_client.metrics.list(name=name, dimensions=dimensions, limit=limit)
        #print names
        return metrics

    # function get measurements
    def get_measurements(self, metrics, start_time=None, end_time=None, limit=None):
        measurements = []

        if start_time == None:
            start_date = datetime.datetime.utcnow() - datetime.timedelta(seconds=3600)
            start_time = start_date.strftime("%Y-%m-%dT%H:%M:%SZ")

        if end_time == None:
            end_date = datetime.datetime.utcnow() - datetime.timedelta(seconds=0)
            end_time = end_date.strftime("%Y-%m-%dT%H:%M:%SZ")

        #print metrics
        for metric in metrics:
            # Invoke the Monasca client
            measurements.append(self.monasca_client.metrics.list_measurements(
                name=metric['name'],
                dimensions=metric['dimensions'],
                start_time=start_time,
                end_time=end_time))

        return measurements

    # TODO  Write live code to generate live stream from Monasca for Online Learning
    def live_monasca(self):
        pass





    # def df_from_measurements(self, group):
    #     i = 0
    #     raw = filter(None, self.measurements)
    #     log = 0;
    #     df = pd.DataFrame()
    #    # print('raw = {} '.format(raw))
    #     for s in raw:
    #         #print('s = {} '.format(s[0]))
    #         if s[0]['measurements'] and s[0]['dimensions']['hostname'] == group:
    #             m = np.array(s[0]['measurements'])
    #             timestamps = m[:, s[0]['columns'].index('timestamp')]
    #             df = pd.DataFrame(index=timestamps)
    #             break;
    #     m = 0;
    #     for measure in raw:
    #         if measure[0]['measurements'] and measure[0]['dimensions']['hostname'] == group:
    #             hostname = group
    #             m = np.array(measure[0]['measurements'])
    #             timestamps = m[:, measure[0]['columns'].index('timestamp')]
    #             # df = pd.DataFrame(index = timestamps)
    #             # getting name
    #             if (log == 1):
    #                 print 'metric : \n'
    #                 print measure[0]['name']
    #             name = measure[0]['name'];
    #             # getting dimensions
    #             if (log == 1):
    #                 print '\n Machine name : \n'
    #                 print measure[0]['dimensions']['hostname']
    #             # Getting measurement
    #             if (log == 1):
    #                 print '\n measurements \n'
    #                 print m  # measure[0]['measurements']
    #
    #             # Measurement into Array
    #
    #             m = np.array(measure[0]['measurements'])
    #
    #             timestamps = m[:, measure[0]['columns'].index('timestamp')]
    #             if (log == 1):
    #                 print timestamps
    #
    #             values = m[:, measure[0]['columns'].index('value')]
    #             if (log == 1):
    #                 print '\n values \n '
    #                 print values
    #
    #             # vars()["df_"+str(i)] =  dict( zip( timestamps, m));
    #
    #             df[name] = m[:, measure[0]['columns'].index('value')];
    #
    #             if (log == 1):
    #                 print 'This is the dataframe' + 'is' + name
    #
    #             # vars()["df_"+str(i)]['hostname'] = hostname;
    #
    #             if (log == 1):
    #                 print ' \n \n ***********  --------------- *********** \n'
    #             i = i + 1;
    #     return df;

    def store_measurements(self,path):
        with open(U.Data_dir+path, 'wb') as outfile:
            json.dump(self.measurements, outfile)


if __name__ == '__main__':
    '''

        Working with Monasca

        Measurements to Dataframe

    '''
    MC = Monasca()
    MC.authenticate()
    # df_Ellis = MC.df_from_measurements('ellis.jaafar.com');
    #print ALL
    MC.request(start_time="2016-11-4T15:55:55.001Z", end_time="2016-12-4T16:55:55.001Z",metrics=U.ALL,dimensions={'service': 'NFV-SDN-testbed'})
    MC.store_measurements("measurements.json")
    #print MC.measurements
    #print type(MC.measurements[4][0])
    #print MC.df_from_measurements('homer.jaafar.com')
   # print type(MC.measurements)
    #MC.df_debug()
    # df_Ellis.head()
    #print MC.df_from_measurements('homer.jaafar.com').head()

    '''

        Connecting to Monasca
    '''
    #resp = MC.monasca_client.metrics.list()
    #print type(resp)
    #write_list("Data/response_monasca.txt",resp)
    #check error here

