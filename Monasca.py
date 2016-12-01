from monascaclient import client
from monascaclient import ksclient
import sys
from Util import *
from Password import *
import os

class Monasca:
    database = None
    ks = None
    monasca_client = None
    metrics = []
    measurements = []

    def __init__(self):
        ##
        ## The bug is HERE
        ## You SHould read Measurement as a list not as a String
        ##
        self.measurements = read_file("Data/Measurements.txt")

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

    def request(self, start_time="2016-09-17T15:50:26.0Z", end_time="2016-09-17T15:55:55.0Z", metrics=['net.out_packets_sec']):
       # try:
        self.metrics = self.get_metrics(names=metrics)
       # The error was HEre self.metrics instead of metrics
        self.measurements = self.get_measurements(self.metrics, start_time, end_time)


    def df_from_measurements(self):
        pass

    def show_measurements(self):
        print self.measurements

    # getting the metrics information
    def get_metrics(self, names=[None], dimensions={}, limit=100):
        metrics = []
        for name in names:
            # Invoke the Monasca client
            metrics = metrics + self.monasca_client.metrics.list(name=name, dimensions=dimensions,limit=limit)
        return metrics


    # function get measurements
    def get_measurements(self, metrics, start_time=None, end_time=None, limit=None):


        if start_time == None:
            start_date = datetime.datetime.utcnow() - datetime.timedelta(seconds=3600)
            start_time = start_date.strftime("%Y-%m-%dT%H:%M:%SZ")

        if end_time == None:
            end_date = datetime.datetime.utcnow() - datetime.timedelta(seconds=0)
            end_time = end_date.strftime("%Y-%m-%dT%H:%M:%SZ")

        #print('metrics = {}'.format(metrics))
        for metric in metrics:
            # Invoke the Monasca client
            #print('metric = {}'.format(metric))
            self.measurements.append(self.monasca_client.metrics.list_measurements(
                name=metric['name'],
                dimensions=metric['dimensions'],
                start_time=start_time,
                end_time=end_time))

        return self.measurements

        return measurements

    def df_from_measurements(self, group):
        i = 0
        raw = filter(None, self.measurements)
        log = 0;
        df = pd.DataFrame()
        print('raw = {} '.format(raw[1]))
        for s in raw:
            print('s = {} '.format(s[0]))
            if s[0]['measurements'] and s[0]['dimensions']['hostname'] == group:
                m = np.array(s[0]['measurements'])
                timestamps = m[:, s[0]['columns'].index('timestamp')]
                df = pd.DataFrame(index=timestamps)
                break;
        m = 0;
        for measure in raw:
            if measure[0]['measurements'] and measure[0]['dimensions']['hostname'] == group:
                hostname = group
                m = np.array(measure[0]['measurements'])
                timestamps = m[:, measure[0]['columns'].index('timestamp')]
                # df = pd.DataFrame(index = timestamps)
                # getting name
                if (log == 1):
                    print 'metric : \n'
                    print measure[0]['name']
                name = measure[0]['name'];
                # getting dimensions
                if (log == 1):
                    print '\n Machine name : \n'
                    print measure[0]['dimensions']['hostname']
                # Getting measurement
                if (log == 1):
                    print '\n measurements \n'
                    print m  # measure[0]['measurements']

                # Measurement into Array

                m = np.array(measure[0]['measurements'])

                timestamps = m[:, measure[0]['columns'].index('timestamp')]
                if (log == 1):
                    print timestamps

                values = m[:, measure[0]['columns'].index('value')]
                if (log == 1):
                    print '\n values \n '
                    print values

                # vars()["df_"+str(i)] =  dict( zip( timestamps, m));

                df[name] = m[:, measure[0]['columns'].index('value')];

                if (log == 1):
                    print 'This is the dataframe' + 'is' + name

                # vars()["df_"+str(i)]['hostname'] = hostname;

                if (log == 1):
                    print ' \n \n ***********  --------------- *********** \n'
                i = i + 1;
        return df;

    def store_measurements(self,path):
        write_list(path,self.measurements)