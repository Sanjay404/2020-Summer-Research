import plotly.graph_objects as go
import pandas as pd

ALL_DATA= pd.read_csv('/Users/sanjay/Desktop/CODE/Python/2020 Summer Research/DATA/D1.csv')
print('Number of points I am looking at: '+ str((len(ALL_DATA))))
ALL_DATA.head()

#CONTAINS TO AND FROM LAT/LONG
df_flight_paths = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')
df_flight_paths.head() 

fig = go.Figure()

fig.add_trace(go.Scattergeo( 
    locations = ["afria"],
    locationmode = 'geojson-id',
    lon = ALL_DATA['LON'],
    lat = ALL_DATA['LAT'],
    hoverinfo = 'text',
    text = ALL_DATA['Ind_ID'],
    mode = 'markers',
    marker = dict(
        size = 2,
        color = 'rgb(255, 0, 0)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )))

flight_paths = []
'''
for i in range(len(df_flight_paths)): #ACTUALLY ADDS LINES
    fig.add_trace(
        go.Scattergeo(
            locationmode = 'USA-states',
            lon = [df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i]],
            lat = [df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i]],
            mode = 'lines',
            line = dict(width = 1,color = 'red'),
            opacity = float(df_flight_paths['cnt'][i]) / float(df_flight_paths['cnt'].max()),
        )
    )
'''
fig.update_layout(
    title_text = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
    showlegend = False,
    geo = dict(
        scope = 'africa',
        projection_type = 'azimuthal equal area',
        showland = True,
        landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
    ),
)

fig.show()