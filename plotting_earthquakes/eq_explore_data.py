from pathlib import Path
import json
import plotly.express as px

# Read data as a string and convert to Python object
path = Path('../pythonic-data-analysis/eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset
metadata_dict = all_eq_data['metadata']
all_eq_data = all_eq_data['features'] # stores data in a list
# print(len(all_eq_data)) Prints the total number of earthquakes, should be 160

#Initializes empty list
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_data:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)
print(mags[:10]) #sanity check to make sure all data is correct
print(lons[:5])
print(lats[:5])

# Plotting a worldmap
title = metadata_dict['title']
fig = px.scatter_geo(lat=lats, 
                     lon=lons, 
                     size=mags, #uses magnitude of earthquake for dot size
                     title=title,
                     color=mags, #uses magnitude of earthquake for color
                     color_continuous_scale='Viridis',
                     projection='natural earth',
                     hover_name=eq_titles,
)

import plotly.io as pio # always always always import this to make sure the renderer doesnt do stupid stuff
pio.renderers.default = 'browser'

fig.show()

# use the following to see all of the colors available in a REPL
# import plotly.express as px
# px.colors.named_colorscales()