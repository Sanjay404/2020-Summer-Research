import geopy.distance
import math
import csv
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import os
from time import strptime

# plot their releasing sites per origin and year of release
directory = r'/Users/sanjay/Desktop/CODE/Python/2020 Summer Research/release locations/'
# READ IN CSV as List
with open(os.path.join(directory, "data.csv")) as f:
    reader = csv.reader(f)
    csvr = [tuple(line) for line in reader]
print('Number of points I am looking at: ' + str((len(csvr))))
# function that writes each row


def writeRow(fileName, rowNum):
    if csvr[rowNum][3] == 'captive bred':  # adds origin tag to fileName
        fileName = 'cb' + str(fileName)
    else:
        fileName = csvr[rowNum][3] + str(fileName)
    # ERROR SOMEWHERE HERE

    if (os.path.isfile(os.path.join(directory, "SORTED DATA/", f'{fileName}.csv'))):
        opening = 'a'  # append
    else:
        opening = 'w'  # write
        # ERROR SOMEHWHERE HERE
    with open(os.path.join(directory, "SORTED DATA/", f'{fileName}.csv'), opening, newline='') as file:
        writer = csv.writer(file)
        if opening == 'w':
            writer.writerow(["Ind_ID", "Npoints_beforecleaning", "Npoints_aftercleaning1",
                             "Origin", "Release_Date", "Release_Lat", "Release_Lon", "Country"])
        writer.writerow(csvr[rowNum])
        # global count
       # count += 1
   # print(count)


# Split DATA INTO DIFFERENT CSVS
for i in range(1, len(csvr)):
    temp = strptime(csvr[i][4], '%m/%d/%Y').tm_year
    if temp == 2014:
        writeRow('2014', i)
    elif temp == 2015:
        writeRow('2015', i)
    elif temp == 2016:
        writeRow('2016', i)
    elif temp == 2017:
        writeRow('2017', i)
    elif temp == 2018:
        writeRow('2018', i)
    else:
        print(str(i)+" NOT COPIED")

for fileName in os.listdir(os.path.join(directory, "SORTED DATA")):
    if fileName.endswith(".csv"):
        # Rereading data
        DATA = pd.read_csv(
            (os.path.join(directory, "SORTED DATA", f'{fileName}')))
        # sets zoom
        fig = go.Figure(data=go.Scattergeo(
            lon=DATA['Release_Lat'],
            lat=DATA['Release_Lon'],
            mode='markers',
        ))

        fig.update_layout(
            title=f'{fileName}',
            geo_scope='europe',
        )
        fig.update_geos(
            lataxis_showgrid=True,
            lonaxis_showgrid=True,
        )
        # fig.update_traces(hovertemplate='GDP: %{x} <br>Life Expectany: %{y}')
        # https://plotly.com/python/hover-text-and-formatting/
        # fig.show()


for fileName in os.listdir(os.path.join(directory, "SORTED DATA")):
    if fileName.endswith(".csv"):
        outliers = set()
        temp = pd.read_csv(os.path.join(directory, 'SORTED DATA', fileName))
        cordList = list(zip(temp["Ind_ID"], temp["Npoints_beforecleaning"], temp["Npoints_aftercleaning1"],
                            temp["Origin"], temp["Release_Date"], temp["Release_Lat"], temp["Release_Lon"], temp["Country"]))

        outliers = set()
        for i in cordList:    # finds outliers in release locations (>10km)
            outside = True
            for j in cordList:
                cord1 = (float(i[5]), float(i[6]))
                cord2 = (float(j[5]), float(j[6]))
                if i != j and geopy.distance.distance(cord1, cord2) < 10:
                    outside = False
            if outside:
                outliers.add(i)

        with open(os.path.join(directory, 'OUTLIERS', f'outliers_{fileName}'), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Ind_ID", "Npoints_beforecleaning", "Npoints_aftercleaning1",
                             "Origin", "Release_Date", "Release_Lat", "Release_Lon", "Country"])
            for e in outliers:
                writer.writerow(e)
'''
    for x in range(1, len(csvr)):
        for y in range(2, len(csvr)):
            coord1 = (float(csvr[x][5]), float(csvr[x][6]))
            coord2 = (float(csvr[y][5]), float(csvr[y][6]))
            if(geopy.distance.distance(coord1, coord2).km >= 10):  # DOESNT WORK
                # https://benalexkeen.com/k-means-clustering-in-python/
                outliers.add(tuple(csvr[x]))
                break
'''
# deletes temp csvs
for fileName in os.listdir(os.path.join(directory, "SORTED DATA")):
    os.unlink(os.path.join(directory,  "SORTED DATA", fileName))
