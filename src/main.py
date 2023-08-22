import pandas as pd
import numpy as np
import os

csv_input = pd.read_csv(filepath_or_buffer='/Users/woojyelee/projects/location_cleaner/src/resource/airport_codes.csv', encoding="cp949")
csv_input3 = pd.read_csv(filepath_or_buffer='/Users/woojyelee/projects/location_cleaner/src/resource/airport_location.csv', encoding="cp949")

csv_input3 = csv_input3[csv_input3["type"].str.contains('airport')]

df = pd.concat([csv_input["name"], csv_input3["name"]], axis = 0, ignore_index=True) #기존 index 무시 no
dw = df
de = pd.DataFrame(df)


dd = de.duplicated(subset='name', keep="last") #series
#dd = de.duplicated(subset='name', keep= "last") #series
dt = dd[dd==False] #true가 나온 불린&인덱스를 series로 표현 -> false true ... 형태
#de.index -> 인덱스 나열식..
#v = (df["name"])[dt.index]
#dt = dt[dt.index]

####dt = dt[csv_input["name"] != None] #series != array
#de = de[de[csv_input3["name"] != None]]

cc = csv_input3[["name", "latitude_deg", "longitude_deg"]]

dg = de.duplicated(subset='name', keep="first")
dz = dg[dg==False] #dg, dz: series
#dz = dz[dz.index]
#######dz = dz[dw != None]

t = csv_input[["code", "name"]]

s = pd.merge( t, cc, on="name")

#csv_output = {'name' : dc, 'code' : csv_input["공항코드1(IATA)"], 'location(la)': (csv_input3[csv_input3['name']==dc])["latitude_deg"], 'location(lo)' : (csv_input3[csv_input3['name']==dc])["longitude_deg"]}



#csv_output = {'name' : s["name"], 'code' : s["공항코드1(IATA)"], 'latitude(la)' : s["latitude_deg"], 'longitude(lo)' : s["longitude_deg"]}
print(s)
s.to_csv("output.csv")
