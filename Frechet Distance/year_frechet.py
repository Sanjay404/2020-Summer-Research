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
import inspect, re

'''
GIVEN A Year, I AM GOING TO PLOT THE RELEASE YEARS
'''
class year(object):
    def __init__(self, name):
        self.name = name
        self.list = []
class locality(object):
    def __init__(self, name):
        self.name = name #locality
        self.d2009 = year('2009')
        self.d2010 = year('2010')
        self.d2011 = year('2011')
        self.d2012 = year('2012')
        self.d2013 = year('2013')
        self.d2014 = year('2014')
        self.d2015 = year('2015')
        self.d2016 = year('2016')
        self.d2017 = year('2017')
        self.d2018 = year('2018')
        self.d2019 = year('2019')
        self.release_years = [
            self.d2009,self.d2010,self.d2011,self.d2012,self.d2013,self.d2014,
            self.d2015,self.d2016,self.d2017,self.d2018,self.d2019
            ]
    def get(self,year):
        return self.__getattribute__(year)
class Season(object):
    '''
    Class represents each migration year, with lists for the release years
    '''
    def __init__(self, name):
        self.name = name #represents current season
        self.cb = locality('cb') 
        self.wild = locality('wild')
        self.ECWP = locality('ECWP')
        self.KYZY = locality('KYZY')
        self.NAVOIY = locality('NAVOIY')
        self.SASBETPAK = locality('SASBETPAK')
        self.SASEBALK = locality('SASEBALK')
        self.SKHBCBETPAK = locality('SKHBCBETPAK')
        self.SKHBCUSTY = locality('SKHBCUSTY')
        self.CB_NAV = locality('CB_NAV')
        self.CB_KYZY = locality('CB_KYZY')
        self.locs = [
        self.cb, self.wild, self.ECWP, self.KYZY, self.NAVOIY, self.SASBETPAK, 
        self.SASEBALK, self.SKHBCBETPAK, self.SKHBCUSTY, self.CB_NAV, self.CB_KYZY
        ]
    def get(self, s):
        return self.__getattribute__(s)
def varname(p):
  for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
    m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
    if m:
      return m.group(1)

def str_to_func(locality, request, rel_year):
    #print(request.name, locality, rel_year )
    # 2017, wild, d2016 
    func = {
        '2009': request.get(locality).get(rel_year),
        '2010': request.get(locality).get(rel_year),
        '2011': request.get(locality).get(rel_year),
        '2012': request.get(locality).get(rel_year),
        '2013': request.get(locality).get(rel_year),
        '2014': request.get(locality).get(rel_year),
        '2015': request.get(locality).get(rel_year),
        '2016': request.get(locality).get(rel_year),
        '2017': request.get(locality).get(rel_year),
        '2018': request.get(locality).get(rel_year),
        '2019': request.get(locality).get(rel_year),
    }

    return func.get(request.name)


def plotDataAverage(data):  #data is the list
    dist = []
    for path in data:
        if path.endswith(".csv"):
            df = pd.read_csv(path)
            try:
                avg_dist = sum(df['frechet_dist']) / (len(df['frechet_dist']))
                dist.append(avg_dist)
                return avg_dist
            except Exception as e:
                return 0
def plot(season):
    plt.figure()
    plt.ylabel('Frechet Distance', fontsize=9)
    plt.xlabel('Release Year', fontsize=9)
    plt.title(f'Frechet Distances for {season.name}', fontsize=12)
    for locality in season.locs:
        x,y, locality = b(locality)
        plt.plot(x, y, label = locality)

    #plt.plot(x, y, label = locality)

    ''' plt.savefig(
        fname=
        f'/Users/sanjay/Desktop/CODE/R/bustards/Students/Sanjay/percentLocality.png'
        )
    '''
    plt.legend()
    plt.show()


def a(locality):
        dic = {} #a dictionary for each locality
        for year in locality.release_years:
            if(len(year.list)>0):
                dic[year.name]= plotDataAverage(year.list)     
        if len(dic) == 0:
            return         
        lists = sorted(dic.items())  # sorted by key, return a list of tuples
        locality = locality.name
        x, y = zip(*lists)  # unpack a list of pairs into two tuples
        return x,y, locality


def b(locality):
        x = []
        y = []
        for year in locality.release_years:
            if(len(year.list)>0):
                x.append(year.name)
                y.append(plotDataAverage(year.list))             
        locality = locality.name
        if len(x) == 0:
            return
        zipped = zip(x,y)
        zipped = sorted(zipped, key = lambda x: x[0]) 
        x, y = zip(*zipped) 
        return x,y,locality

'''
for locality in season.locs:
        #dic = {} #a dictionary for each locality
        x = []
        y = []
        for year in locality.release_years:
            if(len(year.list)>0):
                #dic[year.name]= plotDataAverage(year.list)
                x.append(year.name)
                y.append(plotDataAverage(year.list))
                
        if len(x) == 0:
            continue
      
        lists = sorted(dic.items())  # sorted by key, return a list of tuples
        locality = locality.name
        x, y = zip(*lists)  # unpack a list of pairs into two tuples
  
        zipped = zip(x,y)
        zipped = sorted(zipped, key = lambda x: x[0]) 
        x, y = zip(*zipped) 

        plt.plot(x, y, label = locality.name)

  plt.savefig(
            fname=
            f'/Users/sanjay/Desktop/CODE/R/bustards/Students/Sanjay/percentLocality.png'
        )

    plt.legend()
    plt.show()
'''
def main():
    #each season has all the types of breeding, which has each release year
    y2009 =  Season('2009')
    y2010 =  Season('2010')
    y2011 =  Season('2011')
    y2012 =  Season('2012')
    y2013 =  Season('2013')
    y2014 =  Season('2014')
    y2015 =  Season('2015')
    y2016 =  Season('2016')
    y2017 =  Season('2017')
    y2018 =  Season('2018')
    y2019 =  Season('2019')
    base_dir = '/Users/sanjay/Desktop/CODE/Python/2020 Summer Research/Frechet Distance/'
    # list representing all release dates
    seasons = [
        y2009, y2010, y2011, y2012, y2013, y2014, y2015, y2016,
        y2017, y2018, y2019
    ]
    locs = [
        'cb', 'wild', 'ECWP', 'KYZY', 'NAVOIY', 'SASBETPAK', 'SASEBALK', 'SKHBCBETPAK',
        'SKHBCUSTY', 'CB_NAV', 'CB_KYZY'
    ] 
    for folder in os.listdir(os.path.join(base_dir, "data")):
        if not (folder == '.DS_Store'):
            data = os.listdir(os.path.join(base_dir, "data", folder))
            for csv in data:
                if 'DS_Store' in csv:
                    continue
                split = csv.split('_')
                for szn in seasons:
                    if split[-2] == szn.name: # season
                        for loc in locs: #for labels
                            if split[0] == loc:  #checks if localities match
                                if split[1] == 'NAVOIY':
                                    loc = 'CB_NAV'
                                if split[1] == 'KYZY':
                                    loc = 'CB_KYZY'
                                release_year = str('d' + split[-3] )  #for labels
                                str_to_func(loc, szn ,release_year).list.append(
                                    os.path.join(base_dir, "data", folder,
                                                csv))  #add it to the list

    for season in seasons:
        plot(season)
if __name__ == '__main__':
    main()
