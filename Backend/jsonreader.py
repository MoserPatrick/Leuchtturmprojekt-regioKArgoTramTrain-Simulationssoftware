import json
import Station
stationlist = []
names = []
trias_id = []
f = open('Backend/jsonFiles/KVV_Stops_v4.json')
data = json.load(f)
for item in data:
    names.append(item['name'])
    trias_id.append(item['triasID'])
for i in range(len(names)):
    stationlist.append(Station.Station(names[i], trias_id[i]))

    

f.close

d = open('Backend/jsonFiles/KVV_Lines_Stops_Based_v2.json')

lines = []
numbers = []

data = json.load(d)
for item in data['lines']:
    lines.append(item['stations'])
    numbers.append(item['number'])

print(numbers)

for elements in stationlist:
    for i in range (len(lines)):
        for j in range (len(lines[i])):
            if elements.get_triasID() == lines[i][j]:
                elements.add_line(numbers[i])

for element in stationlist :
    print(element.get_name())
    print(element.get_lines())


d.close