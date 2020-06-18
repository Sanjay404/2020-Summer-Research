import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import os

directory = r'/Users/sanjay/Desktop/CODE/Python/2020 Summer Research/'
for fileName in os.listdir(os.path.join(directory+"DATA/")):  # goes through all CSVS
    if fileName.endswith(".csv"):
        # READ IN CSV
        ALL_DATA = pd.read_csv(os.path.join(directory+"DATA/"+str(fileName)))
        print('Number of points I am looking at: ' + str((len(ALL_DATA))))
        longitude = ALL_DATA['LON']
        latitude = ALL_DATA['LAT']
        date = ALL_DATA['Date']
        # list of the Date, lat, long
        sorted_data = list(zip(date, latitude, longitude))
        # SORT DATA BY TIME
        sorted_data.sort(key=lambda timeString: datetime.strptime(
            timeString[0], '%m/%d/%Y %H:%M:%S'), reverse=False)

        # WRITE SORTED_DATA TO CSV
        import csv
        with open(os.path.join(directory+"SORTED DATA/"+f'sorted{fileName}'), 'w', newline='') as file:
            writer = csv.writer(file)
            sorted_data.insert(0, ("Date", "LAT", "LONG"))
            for row in sorted_data:
                writer.writerow(row) 
        # Rereading data
        DATA = pd.read_csv(
            (os.path.join(directory+"SORTED DATA/"+f'sorted{fileName}')))
        # simply plots data points
        fig = go.Figure(data=go.Scattergeo(
            lon=DATA['LONG'],
            lat=DATA['LAT'],
            mode='lines',  # markers
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
