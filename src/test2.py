import pandas as pd
import numpy as np
import os

csv_input = pd.read_csv(filepath_or_buffer='/Users/woojyelee/projects/location_cleaner/src/resource/airport_codes.csv', encoding="cp949")
csv_input3 = pd.read_csv(filepath_or_buffer='/Users/woojyelee/projects/location_cleaner/src/resource/airport_location.csv', encoding="cp949")

csv_input3 = csv_input3[csv_input3["type"].str.contains('airport')]

df = pd.concat([csv_input["name"], csv_input3["name"]], axis = 0, ignore_index=False) #기존 index 무시 no
dw = df
de = pd.DataFrame(df)

cs = csv_input[["공항코드1(IATA)", "name"]]

print(cs)