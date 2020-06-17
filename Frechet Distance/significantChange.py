'''
Ideas is to have a class (which represents a start date) with 
lists (of paths) for each type of release. Should be ~4-5 for each. 
Pass these lists to plot function. Which will go plot entries by the year
(i.e entire csvs at a time).
'''
import math
import csv
import pandas as pd
from datetime import datetime
import os
from time import strptime
import matplotlib.pyplot as plt
import sys

class Year(object):
    '''
    Class represents stating year, with lists of paths to things with 
    same starting year, differentiated by release type
    '''
    def __init__(self, name):
        self.name = name
        self.cb = []
        #ECCH = []
        self.wild = []

def str_to_func(tp, date):
    funCall = { 'cb' : date.cb,
                #'ECCH' : date.ECCH,
                'wild' : date.wild
            }
    return funCall.get(tp)

def plot(data): #data is a list of csv paths to plot 
    #plotting each by intial release date and type
    if(len(data)==0):
        return
    plt.figure(figsize=(20, 6))
    id_dist,dates = plotData(data)
    print(len(dates))
    for key in id_dist.keys() :
        print(len(id_dist.get(key)))
        print(id_dist.get(key))
        plt.plot(dates, id_dist.get(key), label = key)
        plt.title('Categorical Plotting')
        plt.show()
    
def plotData(data):
    if data[0].endswith(".csv"):
        first_data = pd.read_csv(data[0])
        id1 = first_data['id1']
        distances = first_data['frechet_dist']
        temp = zip(id1,distances)
        plot= {}
        print(type(plot))
        for ids,d in temp:
            plot[ids] = [d]
    data_iter = iter(data)
    next(data_iter)
    for path in data_iter:
        if not path.endswith(".csv"):
            continue
        # READ IN CSV
        ALL_DATA = pd.read_csv(path)
        id1 = ALL_DATA['id1']
        distances = ALL_DATA['frechet_dist']
        temp = zip(id1,distances)
        for ids,d in temp:
            if not(plot.get(ids) == None):
                plot.get(ids).append(d)
    dates=[] 
    for path in data:
        split = path.split('_') 
        dates.append(split[-2])
    return plot, dates
def readAsList(path):
    # READ IN CSV as List
    with open(path) as f:
        reader = csv.reader(f)
        csvr = [tuple(line) for line in reader]
        return csvr

def main():
    c2012 = Year('2012')
    c2013 = Year('2013')       
    c2014 = Year('2014')
    c2015 = Year('2015')
    c2016 = Year('2016')
    c2017 = Year('2017')
    c2018 = Year('2018')
    base_dir = '/Users/sanjay/Desktop/CODE/Python/2020 Summer Research/Frechet Distance/'
    dates = [c2012, c2013, c2014, c2015, c2016, c2017, c2018] # classes representing starting dates
    for folder in os.listdir(os.path.join(base_dir, "data")):
        if not (folder == '.DS_Store'):
            imagePaths = os.listdir(os.path.join(base_dir, "data", folder))
            for image in imagePaths:
                if 'DS_Store' in image:
                    continue   
                split = image.split('_') 
                for date in dates:
                    if split[-3] == date.name: #split[1] = release year #date.name
                        tp = split[0]
                        if tp == 'cb' or tp == 'wild':
                            str_to_func(tp, date).append(os.path.join(base_dir, 
                            "data", folder, image))
                            #image.replace('.csv', '')
    for date in dates:
        plot(date.cb)
        plot(date.wild)


if __name__ == '__main__':
    main()