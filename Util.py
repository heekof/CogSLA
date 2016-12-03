import datetime
import time
import logging
# Import libraries use for visualization and analysis
import pandas as pd
import numpy as np
import datetime
import yaml

#import cufflinks as cf

ALL = ['net.out_packets_sec', 'cpu.idle_perc', 'cpu.stolen_perc', 'cpu.system_perc', 'cpu.wait_perc',
       'disk.inode_used_perc', 'disk.space_used_perc', 'host_alive_status', 'http_status', 'io.read_kbytes_sec',
       'io.read_req_sec', 'io.read_time_sec', 'io.write_kbytes_sec', 'io.write_req_sec', 'io.write_time_sec',
       'load.avg_15_min', 'load.avg_1_min', 'load.avg_5_min', 'mem.free_mb', 'mem.total_mb', 'mem.usable_perc',
       'mem.usable_mb', 'net.in_bytes_sec', 'net.in_errors_sec', 'net.in_packets_dropped_sec', 'net.in_packets_sec',
       'net.out_bytes_sec', 'net.out_errors_sec', 'process.cpu_perc', 'process.mem.rss_mbytes']

def Timestamp(df):
    tsp = np.array(df.index)
    string_date = np.array(df.index)
    i = 0;
    for ind in tsp:
        tsp[i] = time.mktime(datetime.datetime.strptime(repr(str(ind))[1:-1], '%Y-%m-%dT%H:%M:%S.%fZ').timetuple())
        # string_date[i]=datetime.datetime.fromtimestamp(int(tsp[i])).strftime('%Y-%m-%d %H:%M:%S')
        string_date[i] = datetime.datetime.utcfromtimestamp(tsp[i])
        i += 1;

    return string_date


def yaml_load(file_path):
    ''' Read Data from a YAML file '''
    with open(file_path, 'r') as file_descriptor:
        data = yaml.load(file_descriptor)
    return data


def yaml_dump(file_path):
    ''' Dump Data to a YAML file '''
    with open(file_path, 'w') as file_descriptor:
        yaml.dump(data, file_descriptor)





def read_file(path):
    file = open(path, 'r')
    content = file.read()
    return content

def write_file(path,content):
    file = open(path, "w")
    file.write(content)
    file.close()

def write_list(path,thelist):
    file = open(path, "w")
    for item in thelist:
        file.write("%s\n" % item)
    file.close()

def printVar(a,b=3,*args,**kwargs):
    print 'a = {} and b  = {} and c = {} '.format(a,b,args[0])

    for key,value in kwargs.iteritems():
        print 'key = {} , value = {} '.format(key,value)

    return True
def deleteContent(path):
    open(path,'w').close()

def initLog(path,debug=0):
    logger = logging.getLogger(__name__)
    deleteContent(path)
    logger.setLevel(logging.DEBUG)
    # create a file handler
    handler = logging.FileHandler(path)
    handler.setLevel(logging.DEBUG)
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(handler)
    if not debug:
        logging.disable(logging.DEBUG)
    return logger






def stamped_df(dframe):

    dframe['Timestamp']=Timestamp(dframe)
    dframe.index.names = [None]
    dframe = dframe.reset_index(drop=True)
    dframe = dframe.set_index('Timestamp')


    return dframe



def current_time(T):
    ts_epoch = t.mktime(dt.datetime.strptime(repr(str(T))[1:-1], '%Y-%m-%dT%H:%M:%S.%fZ').timetuple())
    ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    # curt_t = strftime('%Y-%m-%dT%H:%M:%S.0Z', gmtime())
    # current_time(curt_t)
    # datetime.datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    return ts


# Compute a the percentage change of an array
def percentage_change(X):
    return [100.0 * a1 / a2 - 100 for a1, a2 in zip(X[1:], X)]


# df in percentage
def perc_df(df):
    for i in range(len(df.columns)):
        metric_name = df.columns[i]
        df[metric_name] = np.append([1], percentage_change(df[metric_name].values))

    return df


def to_vect(X, w):
    inputs = [[X[i + e] for e in range(w)] for i in range(len(X) - w)]
    targets = [[X[j + w]] for j in range(len(X) - w)]

    return inputs, targets


def to_vect2(X, w):
    inputs = [[X[i + e] for e in range(w)] for i in range(len(X) - w)]
    targets = [X[j + w] for j in range(len(X) - w)]

    return np.array(inputs), np.array(targets)


# getting the prediction in the form of an array
def get_prediction():
    i = 0;
    for inp in inputs:
        error = pow(nn.predict(inputs[i])[0] - targets[i][0], 2);
        print ' \n The input is : \n\n ' + str(inputs[i]) + '\n\n the target is : \n\n ' + str(
            targets[i]) + '\n\n the predicted value is : \n\n ' + str(
            nn.predict(inputs[i])) + '\n\n The error is : \n\n ' + str(error) + ' \n\n *** \n\n '
        i += 1;
        time.sleep(5)