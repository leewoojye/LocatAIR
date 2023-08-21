import pandas as pd

a = [3,5,2,7,4]

b = pd.Series(a)
print(b)

print(a.index(3))
print(a[3])

print(b.index[3])
#print(b.index(2))
b = pd.DataFrame(b)
c = b.to_dict('list')
print(c)
print(c[0][1])

print(len(c[0]))

# csv_output = {'name' : cc[de.index], 'code' : csv_input[de.index]["공항코드1(IATA)"], 'location(la)' : csv_input3["latitude_deg"][de.index], 'location(lo)' : csv_input3["longitude_deg"][de.index]}