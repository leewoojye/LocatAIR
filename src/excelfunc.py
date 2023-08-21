import pandas as pd
import numpy as np
import os

csv_input = pd.read_csv(filepath_or_buffer='/Users/woojyelee/projects/location_cleaner/src/resource/airport_codes.csv', encoding="cp949")
csv_input3 = pd.read_csv(filepath_or_buffer='/Users/woojyelee/projects/location_cleaner/src/resource/airport_location.csv', encoding="cp949")

csv_input2 = csv_input[["name", "공항코드1(IATA)"]]
csv_input4 = csv_input3[["name", "latitude_deg", "longitude_deg"]]

df = pd.concat([csv_input["name"], csv_input3["name"]], axis = 0)
de = pd.DataFrame(df)

#print(csv_input2.size) #항목 수 반환: 행*칼럼 수
#print(csv_input4.size) #항목 수 반환: 행*칼럼 수

#df = (pd.Series(csv_input3["name"])).append(pd.Series(csv_input["name"]))

#dd = df.duplicated(['name'], keep='False') #series type
#dt = df[[df.duplicated(['name'], keep=False)]==True]
#dd = df[dt==True]
#dd = df[df[csv_input['name'] == csv_input3['name']]]

dd = de.duplicated(subset='name', keep="last")

dc = pd.DataFrame(dd)


c = csv_input3["latitude_deg"] #series type
e = csv_input3["longitude_deg"]

csv_output = {'name' : dc, 'code' : csv_input["공항코드1(IATA)"], 'location(la)': (csv_input3[csv_input3['name']==dc])["latitude_deg"], 'location(lo)' : (csv_input3[csv_input3['name']==dc])["longitude_deg"]}

print(pd.DataFrame(csv_output))

a = pd.DataFrame(csv_output)
#a.to_csv("output.csv")
print(type(dd))