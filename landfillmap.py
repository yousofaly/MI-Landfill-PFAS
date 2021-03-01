# -*- coding: utf-8 -*-
"""LandfillMap.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/yousofaly/MI-Landfill-PFAS/blob/master/LandfillMap.ipynb
"""

import pandas as pd
from geopy.geocoders import Nominatim 
!pip install geocoder
import geocoder
import folium
from folium.plugins import FloatImage

t42a = pd.read_excel(r"C:\Users\yousof.aly\Desktop\Tasks\WWW\MI_landfill_PFAS.xlsx" , sheet_name = 'Table 4-2A')
t42ba = pd.read_excel(r"C:\Users\yousof.aly\Desktop\Tasks\WWW\MI_landfill_PFAS.xlsx" , sheet_name = 'Table 4-2BA')
t42bb = pd.read_excel(r"C:\Users\yousof.aly\Desktop\Tasks\WWW\MI_landfill_PFAS.xlsx" , sheet_name = 'Table 4-2BB')
t42bc = pd.read_excel(r"C:\Users\yousof.aly\Desktop\Tasks\WWW\MI_landfill_PFAS.xlsx" , sheet_name = 'Table 4-2BC')

address = 'Michigan'

geolocator = Nominatim(user_agent="MI_explorer", timeout = 3)
location = geolocator.geocode(address)
milat = location.latitude
milong = location.longitude
print('The geograpical coordinate of Michigan are {}, {}.'.format(milat, milong))

addresses = t42a.iloc[:,1]
lat = []
lng = []
for address in addresses:
    location = geolocator.geocode(address)
    try:
        lat.append(location.latitude)
        lng.append (location.longitude)
    except: 
        lat.append('NA')
        lng.append ('NA')
        
t42a['Lat'] = lat
t42a['Lng'] = lng
t42a[t42a['Lat'] == 'NA']

t42a.at[0, 'Lat'] = 42.410534
t42a.at[0, 'Lng'] = -83.562455

t42a.at[3, 'Lat'] = 42.362980
t42a.at[3, 'Lng'] = -85.033675

t42a.at[6, 'Lat'] = 42.911375
t42a.at[6, 'Lng'] = -83.724699

t42a.at[9, 'Lat'] = 44.788840
t42a.at[9, 'Lng'] = -85.847909

t42a.at[10, 'Lat'] = 42.789759
t42a.at[10, 'Lng'] = -84.691708

t42a.at[12, 'Lat'] = 46.786463
t42a.at[12, 'Lng'] = -89.128742

t42a.at[18, 'Lat'] = 42.174334
t42a.at[18, 'Lng'] = -86.283150

t42a.at[20, 'Lat'] = 43.283096
t42a.at[20, 'Lng'] = -83.871234

t42a.at[22, 'Lat'] = 43.104132
t42a.at[22, 'Lng'] = -85.170941

t42a.at[25, 'Lat'] = 43.437032 
t42a.at[25, 'Lng'] = -82.731291

t42a.at[28, 'Lat'] = 44.858289
t42a.at[28, 'Lng'] = -84.665372

t42a

addresses = t42ba.iloc[:,0]
lat = []
lng = []
for address in addresses:
    location = geolocator.geocode(address+', MI')
    try:
        lat.append(location.latitude)
        lng.append (location.longitude)
    except: 
        lat.append('NA')
        lng.append ('NA')

t42ba['Lat'] = lat
t42ba['Lng'] = lng

t42ba.at[3, 'Lat'] = 43.195628
t42ba.at[3, 'Lng'] = -83.856839

t42ba.at[10, 'DF'] = 'Sandusky'
t42ba.at[10, 'Lat'] = 43.420024
t42ba.at[10, 'Lng'] = -82.831913

t42ba.at[12, 'Lat'] = 42.885267
t42ba.at[12, 'Lng'] = -85.724076

t42ba.at[13, 'Lat'] = 42.260503
t42ba.at[13, 'Lng'] = -83.554378

t42ba.at[6, 'Lat'] = 42.645914
t42ba.at[6, 'Lng'] = -85.289454

t42ba

addresses = t42bb.iloc[:,0]
lat = []
lng = []
for address in addresses:
    location = geolocator.geocode(address+', MI')
    try:
        lat.append(location.latitude)
        lng.append (location.longitude)
    except: 
        lat.append('NA')
        lng.append ('NA')

t42bb['Lat'] = lat
t42bb['Lng'] = lng

t42bb.at[0, 'Lat'] = 43.595294
t42bb.at[0, 'Lng'] =-83.890217

t42bb.at[4, 'Lat'] = 46.343187
t42bb.at[4, 'Lng'] = -87.386007

t42bb.at[6, 'Lat'] = 43.059467 
t42bb.at[6, 'Lng'] = -85.610112

t42bb.at[8, 'Lat'] = 42.101199
t42bb.at[8, 'Lng'] =-83.405800

t42bb

addresses = t42bc.iloc[:,0]
lat = []
lng = []
for address in addresses:
    location = geolocator.geocode(address+', MI')
    try:
        lat.append(location.latitude)
        lng.append (location.longitude)
    except: 
        lat.append('NA')
        lng.append ('NA')

t42bc['Lat'] = lat
t42bc['Lng'] = lng

t42bc.at[1, 'DF'] = 'Alpena'
t42bc.at[1, 'Lat'] = 45.066839
t42bc.at[1, 'Lng'] = -83.440254

t42bc.at[14, 'Lat'] = 43.092527
t42bc.at[14, 'Lng'] = -83.615214

t42bc.at[29, 'DF'] = 'Saginaw'
t42bc.at[29, 'Lat'] = 43.419596
t42bc.at[29, 'Lng'] = -83.949757

t42bc.at[33, 'Lat'] = 44.290062 
t42bc.at[33, 'Lng'] = -83.492349

t42bc.at[35, 'DF'] = 'West Bay County Regional'
t42bc.at[35, 'Lat'] = 43.628047
t42bc.at[35, 'Lng'] = -83.870574

t42bc.at[37, 'Lat'] = 42.806643
t42bc.at[37, 'Lng'] = -86.015066

t42bc.at[8, 'Lat'] = 42.563476
t42bc.at[8, 'Lng'] = -84.834584

t42bc.at[16, 'Lat'] = 43.177176
t42bc.at[16, 'Lng'] = -85.250912

t42bc.at[20, 'Lat'] = 42.266658
t42bc.at[20, 'Lng'] = -84.409991

t42bc.at[25, 'Lat'] = 42.084682
t42bc.at[25, 'Lng'] = -83.688084

t42bc.at[30, 'Lat'] = 42.167012
t42bc.at[30, 'Lng'] = -83.783421

t42bc.at[10, 'Lat'] = 42.626582
t42bc.at[10, 'Lng'] = -84.531456

t42bc.at[7, 'Lat'] = 41.872532
t42bc.at[7, 'Lng'] = -85.195144

t42bc.at[24, 'Lat'] = 42.912956
t42bc.at[24, 'Lng'] = -82.486436


t42bc

map = folium.Map(location=[milat, milong], zoom_start = 7)
for location in t42a.itertuples():
    label = 'Landfill: {}, PFOA (ppt): {:.0f}, PFOS (ppt): {:.0f}, PFOS+PFOA (ppt): {:.0f}'.format(location[1], location[3], location[4], (location[3]+location[4]))
    label = folium.Popup(label, parse_html = True)
    folium.CircleMarker([location[-2], location[-1]],
                       radius =1,
                      color = 'blue',
                      fill = True,
                      fill_color='#3186cc',
                      fill_opacity = 0.7,
                       parase_html=False).add_to(map)
    folium.Circle(radius=(location[4]+location[5]*20), 
                 popup=label, 
                 location=[location[-2], location[-1]], 
                 color='#3186cc', 
                 fill=True, 
                 fill_color='#3186cc').add_to(map)
for location in t42ba.itertuples():
    label = 'WRRF: {}, PFOA (ppt): {:.0f}, PFOS (ppt): {:.0f}, PFOS+PFOA (ppt): {:.0f}'.format(location[1], location[3], location[4], (location[3]+location[4]))
    label = folium.Popup(label, parse_html = True)
    folium.CircleMarker([location[-2], location[-1]],
                      radius =1,
                      color = 'red',
                      fill = True,
                      fill_color='red',
                      fill_opacity = 0.7,
                       parase_html=False).add_to(map)
    folium.Circle(radius=(location[3]+location[4]*20), 
                 popup=label, 
                 location=[location[-2], location[-1]], 
                 color='red', 
                 fill=True, 
                 fill_color='red').add_to(map)
    
for location in t42bb.itertuples():
    label = 'WRRF: {}, PFOA (ppt): {:.0f}, PFOS (ppt): {:.0f}, PFOS+PFOA (ppt): {:.0f}'.format(location[1], location[3], location[4], (location[3]+location[4]))
    label = folium.Popup(label, parse_html = True)
    folium.CircleMarker([location[-2], location[-1]],
                      radius =1,
                      color = 'green',
                      fill = True,
                      fill_color='green',
                      fill_opacity = 0.7,
                       parase_html=False).add_to(map)
    folium.Circle(radius=(location[3]+location[4]*20), 
                 popup=label, 
                 location=[location[-2], location[-1]], 
                 color='green', 
                 fill=True, 
                 fill_color='green').add_to(map)
    
for location in t42bc.itertuples():
    label = 'WRRF: {}, PFOA (ppt): {:.0f}, PFOS (ppt): {:.0f}, PFOS+PFOA (ppt): {:.0f}'.format(location[1], location[3], location[4], (location[3]+location[4]))
    label = folium.Popup(label, parse_html = True)
    folium.CircleMarker([location[-2], location[-1]],
                      radius =1,
                      color = 'orange',
                      fill = True,
                      fill_color='orange',
                      fill_opacity = 0.7,
                       parase_html=False).add_to(map)
    folium.Circle(radius=(location[3]+location[4]*20), 
                 popup=label, 
                 location=[location[-2], location[-1]], 
                 color='orange', 
                 fill=True, 
                 fill_color='orange').add_to(map)
    
map

"""![legend.PNG](attachment:legend.PNG)"""

map.save('index.html')

