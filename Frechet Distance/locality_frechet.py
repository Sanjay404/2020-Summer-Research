import math
import csv
import pandas as pd
from datetime import datetime
import os
from time import strptime
import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib.ticker as ticker
'''
GIVEN A GROUP, I AM GOING TO PLOT THE DISTANCE PER SEASON
'''


class locality(object):
    '''
    Class represents each migration year, with lists of paths to csvs
    '''
    def __init__(self, name):
        self.name = name
        self.d2009_2010 = []
        self.d2010_2011 = []
        self.d2011_2012 = []
        self.d2012_2013 = []
        self.d2013_2014 = []
        self.d2014_2015 = []
        self.d2015_2016 = []
        self.d2016_2017 = []
        self.d2017_2018 = []
        self.d2018_2019 = []
        self.d2019_2020 = []


def writeRow(tple):
    directory = '/Users/sanjay/Desktop/CODE/Python/2020 Summer Research/Frechet Distance/StandError.csv'
    if (os.path.isfile(directory)):
        opening = 'a'  # append
    else:
        opening = 'w'  # write
    with open(directory, opening, newline='') as file:
        writer = csv.writer(file)
        if opening == 'w':
            writer.writerow(["Locality", "Migration Year", "Standard Error"])
        writer.writerow(tple)


def str_to_func(tp, locality):
    func = {
        'd2009_2010': locality.d2009_2010,
        'd2010_2011': locality.d2010_2011,
        'd2011_2012': locality.d2011_2012,
        'd2012_2013': locality.d2012_2013,
        'd2013_2014': locality.d2013_2014,
        'd2014_2015': locality.d2014_2015,
        'd2015_2016': locality.d2015_2016,
        'd2016_2017': locality.d2016_2017,
        'd2017_2018': locality.d2017_2018,
        'd2018_2019': locality.d2018_2019,
        'd2019_2020': locality.d2019_2020,
    }
    return func.get(tp)


def plotDataAverage(data):  #data is the list
    dist = []
    for path in data:
        if path.endswith(".csv"):
            df = pd.read_csv(path)
            split = path.split('/')
            name = split[-1]
            name = name.replace('.csv', '')
            name = name.split('_')
            try:
                avg_dist = sum(df['frechet_dist']) / (len(df['frechet_dist']))
                dist.append(avg_dist)
                temp = []
                # standard error
                for i in df['frechet_dist']:
                    temp.append(pow((i - avg_dist), 2))
                stdev = (sum(temp) / (len(df['frechet_dist']) - 1))**(0.5)
                stdError = stdev / (len(df['frechet_dist'])**(0.5))
                writeRow((name[0], str(split[-2] + 'to' + split[-1]),
                          str(stdError)))  #0 = locality, -2 = season,
                return avg_dist
            except Exception as e:
                return 0


def main():
    cb = locality('cb')
    wild = locality('wild')
    ECWP = locality('ECWP')
    KYZY = locality('KYZY')
    NAVOIY = locality('NAVOIY')
    SASBETPAK = locality('SASBETPAK')
    SASEBALK = locality('SASEBALK')
    SKHBCBETPAK = locality('SKHBCBETPAK')
    SKHBCUSTY = locality('SKHBCUSTY')
    CB_NAV = locality('CB NAVOIY')
    CB_KYZY = locality('CB KYZY')

    base_dir = '/Users/sanjay/Desktop/CODE/Python/2020 Summer Research/Frechet Distance/'
    locs = [
        cb, wild, ECWP, KYZY, NAVOIY, SASBETPAK, SASEBALK, SKHBCBETPAK,
        SKHBCUSTY, CB_NAV, CB_KYZY
    ]  # classes representing starting dates
    for folder in os.listdir(os.path.join(base_dir, "data")):
        if not (folder == '.DS_Store'):
            imagePaths = os.listdir(os.path.join(base_dir, "data", folder))
            for image in imagePaths:
                if 'DS_Store' in image:
                    continue
                split = image.split('_')
                for loc in locs:
                    if split[0] == loc.name:  #checks if seasons match
                        if split[1] == 'NAVOIY':
                            loc = CB_NAV
                        if split[1] == 'KYZY':
                            loc = CB_KYZY
                        tp = str('d' + split[-2] + '_' +
                                 split[-1])  #for labels
                        tp = tp.replace(".csv", "")
                        tp = str('d' + split[-2] + '_' +
                                 split[-1])  #for labels
                        tp = tp.replace(".csv", "")
                        str_to_func(tp, loc).append(
                            os.path.join(base_dir, "data", folder,
                                         image))  #add it to the list

    plt.figure()
    plt.ylabel('Frechet Distance as Percentage', fontsize=9)
    plt.xlabel('Season', fontsize=9)

    for loc in locs:
        dic = {
            '2009': plotDataAverage(loc.d2009_2010),
            '2010': plotDataAverage(loc.d2010_2011),
            '2011': plotDataAverage(loc.d2011_2012),
            '2012': plotDataAverage(loc.d2012_2013),
            '2013': plotDataAverage(loc.d2013_2014),
            '2014': plotDataAverage(loc.d2014_2015),
            '2015': plotDataAverage(loc.d2015_2016),
            '2016': plotDataAverage(loc.d2016_2017),
            '2017': plotDataAverage(loc.d2017_2018),
            '2018': plotDataAverage(loc.d2018_2019),
            '2019': plotDataAverage(loc.d2019_2020),
        }
        # x-axis is the season
        # y-axis is the distance
        lists = sorted(dic.items())  # sorted by key, return a list of tuples
        x, tempy = zip(*lists)  # unpack a list of pairs into two tuples
        tempy = list(tempy)
        first = 0
        for i in range(len(tempy) - 1):
            if tempy[i] == None:
                continue
            else:
                first = i
                break
        y = []
        for dis in tempy:
            try:
                y.append((float(dis) / tempy[first]) - 1)
            except:
                y.append(None)
        plt.plot(x, y, label=loc.name)
        plt.title(
            f'Average Change in Frechet Distances For Bustards Based off Locality',
            fontsize=12)
        plt.savefig(
            fname=
            f'/Users/sanjay/Desktop/CODE/R/bustards/Students/Sanjay/percentLocality.png'
        )
        #plt.clf()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
