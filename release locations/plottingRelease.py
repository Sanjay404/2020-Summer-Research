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


#count = 0


def writeRow(fileName, rowNum):
    if csvr[rowNum][3] == 'captive bred':  # adds origin tag to fileName
        fileName = 'cp' + str(fileName)
    else:
        fileName = csvr[rowNum][3] + str(fileName)
    # ERROR SOMEWHERE HERE

    if (os.path.isfile(os.path.join(directory, "SORTED DATA/", f'{fileName}.csv'))):
        opening = 'a'
    else:
        opening = 'w'
        # ERROR SOMEHWHERE HERE
    with open(os.path.join(directory, "SORTED DATA/", f'{fileName}.csv'), opening, newline='') as file:
        writer = csv.writer(file)
        writer.writerow(csvr[rowNum])
        #global count
       # count += 1
   # print(count)
# GOTTA ADD HEADERS AFTER --> writer.writerow("Date", "LAT", "LONG")
# DictWriter.writeheader()


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

'''
# Rereading data
DATA = pd.read_csv(
    (os.path.join(directory+"SORTED DATA/"+f'sorted{fileName}')))
# simply plots data points
fig = go.Figure(data=go.Scattergeo(
    lon=DATA['LONG'],
    lat=DATA['LAT'],
    mode='markers',  
))

sex = ALL_DATA['Sex']
fig.update_layout(
    title=f'Bustard {fileName}; Sex: {sex[1]} ',
    geo_scope='asia',
)
fig.update_geos(
    lataxis_showgrid=True,
    lonaxis_showgrid=True,
    showlakes=True,
    lakecolor="Green",
    showrivers=True,
    rivercolor="Green"
)
fig.show()
'''
for fileName in os.listdir(os.path.join(directory, "/SORTED DATA")):
    os.unlink(os.path.join(directory,  "/SORTED DATA", fileName))
