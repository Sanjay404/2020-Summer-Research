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
        self.wild = []
        self.KYZY = []
        self.ECWP = []
        self.NAVOIY = []
        self.SKHBCBETPAK = []
        self.SASEBALK = []
        self.SASBETPAK = []
def str_to_func(tp, date):
    funCall = { 'cb' : date.cb,
               'ECWP' : date.ECWP,
                'KYZY'  : date.KYZY,
                'NAVOIY': date.NAVOIY, 
                'SKHBCBETPAK' : date.SKHBCBETPAK,
                'wild' : date.wild,
                'SASEBALK' : date.SASEBALK,
                'SASBETPAK': date.SASBETPAK
            }
    return funCall.get(tp)
import numpy as np
import matplotlib.ticker as ticker

def plot(year): #data is the class to plot    
    fig, axs = plt.subplots(ncols=2, nrows=4,constrained_layout=True,  sharey = True, sharex = False)
    x, y = 0, 0
    if not len(year.cb)==0:
        value, name = plotDataAverage(year.cb)
        axs[x][y].xaxis.set_major_locator(ticker.MultipleLocator(1))
        if(len(value) == 1):
            axs[x][y].plot(name, value, marker='o', markersize=4, color="blue")
        else:
            axs[x][y].plot(name, value)
        axs[x][y].title.set_text('Captive Bred') 

    x, y = 0, 1  
    if not len(year.wild)==0:
        value, name = plotDataAverage(year.wild)
        axs[x][y].xaxis.set_major_locator(ticker.MultipleLocator(1))
        if len(value) == 1:
            axs[x][y].plot(name, value, marker='o', markersize=4, color="red")

        else:
            axs[x][y].plot(name, value)
        axs[x][y].plot(name, value)
        axs[x][y].title.set_text('Wild')
        
    x, y = 1, 0
    if not len(year.ECWP)==0:
        value, name = plotDataAverage(year.ECWP)
        axs[x][y].xaxis.set_major_locator(ticker.MultipleLocator(1))
        if len(value) == 1:
            axs[x][y].plot(name, value, marker='o', markersize=4, color="red")
        else:
            axs[x][y].plot(name, value)
        axs[x][y].plot(name, value)
        axs[x][y].title.set_text('Separated ECWP')

    x, y = 1, 1
    if not len(year.KYZY)==0:
        value, name = plotDataAverage(year.KYZY)
        axs[x][y].xaxis.set_major_locator(ticker.MultipleLocator(1))
        if len(value) == 1:
            axs[x][y].plot(name, value, marker='o', markersize=4, color="red")

        else:
            axs[x][y].plot(name, value)
        axs[x][y].plot(name, value)
        axs[x][y].title.set_text('Separated KYZY')

    x, y = 2, 0
    if not len(year.NAVOIY)==0:
        value, name = plotDataAverage(year.NAVOIY)
        axs[x][y].xaxis.set_major_locator(ticker.MultipleLocator(1))
        if len(value) == 1:
            axs[x][y].plot(name, value, marker='o', markersize=4, color="red")
        else:
            axs[x][y].plot(name, value)
        axs[x][y].plot(name, value)
        axs[x][y].title.set_text('Separated NAVOIY')

    x, y = 2, 1
    if not len(year.SKHBCBETPAK)==0:
        value, name = plotDataAverage(year.SKHBCBETPAK)
        axs[x][y].xaxis.set_major_locator(ticker.MultipleLocator(1))
        if len(value) == 1:
           axs[x][y].plot(name, value, marker='o', markersize=4, color="red")
        else:
            axs[x][y].plot(name, value)
        axs[x][y].plot(name, value)
        axs[x][y].title.set_text('Separated SKHBCBETPAK')

    x, y = 3, 0
    if not len(year.SASEBALK)==0:
        value, name = plotDataAverage(year.SASEBALK)
        axs[x][y].xaxis.set_major_locator(ticker.MultipleLocator(1))
        if len(value) == 1:
           axs[x][y].plot(name, value, marker='o', markersize=4, color="red")
        else:
            axs[x][y].plot(name, value)
        axs[x][y].plot(name, value)
        axs[x][y].title.set_text('Separated SASEBALK')
    x, y = 3, 1
    if not len(year.SASBETPAK)==0:
        value, name = plotDataAverage(year.SASBETPAK)
        axs[x][y].xaxis.set_major_locator(ticker.MultipleLocator(1))
        if len(value) == 1:
           axs[x][y].plot(name, value, marker='o', markersize=4, color="red")
        else:
            axs[x][y].plot(name, value)
        axs[x][y].plot(name, value)
        axs[x][y].title.set_text('Separated SASBETPAK')

    fig.suptitle(f'Average Change in Frechet Distances For Bustards Released in {year.name}')
    fig.show()

def writeRow(tple):
    directory = '/Users/sanjay/Desktop/CODE/Python/2020 Summer Research/Frechet Distance/StandError.csv'
    if (os.path.isfile(directory)):
        opening = 'a'  # append
    else:
        opening = 'w'  # write
    with open(directory, opening, newline='') as file:
        writer = csv.writer(file)
        if opening == 'w':
            writer.writerow(["Release Year", "Migration Year", "Standard Error"])
        writer.writerow(tple)

def plotDataAverage(data): #data is the list
    plot= {} #dict where key is the season and val is avg dist
    split = data[0].split('_') # for plot name
    dates=[] 
    dist=[]
    for path in data:
        if path.endswith(".csv"):
            splitb = path.split('_') 
            dates.append(splitb[-2])
    for path in data:
        if path.endswith(".csv"):
            df = pd.read_csv(path) 
            split = path.split('_') 
            try:
                avg_dist = sum(df['frechet_dist'])/(len(df['frechet_dist']))
                dist.append(avg_dist) # I KNOW THIS IS RIGHT, because its plotting 
                temp = []
                for i in df['frechet_dist']: #
                    temp.append(pow((i - avg_dist), 2))
                stdev = (sum(temp)/(len(df['frechet_dist'])-1))**(0.5)
                stdError = stdev/(len(df['frechet_dist'])**(0.5))
                writeRow((split[-3], split[-2], str(stdError)))
            except:
                dist.append(0)
    zipped = zip(dist,dates)
    zipped = sorted(zipped, key = lambda t: t[1])
    return list(zip(*zipped)) 

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
                    if split[-3] == date.name: #split[1] = release year  
                        tp = split[0]
                        str_to_func(tp, date).append(os.path.join(base_dir, "data", folder, image))
                        #image.replace('.csv', '')
                            
    for date in dates:
        #pass in each class
        plot(date)

if __name__ == '__main__':
    main()