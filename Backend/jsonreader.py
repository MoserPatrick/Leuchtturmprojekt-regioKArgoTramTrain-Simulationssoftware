import json
import Station

stationlist = []
names = []
trias_id = []
#opens KVV Stops File
f = open('Backend/jsonFiles/KVV_Stops_v4.json')
data = json.load(f)
#TODO get coodinates form All Stops File and save them in stationlist Array
#gets name and trias id form file for each station
for item in data:
    names.append(item['name'])
    trias_id.append(item['triasID'])
for i in range(len(names)):
    stationlist.append(Station.Station(names[i], trias_id[i]))

    
#closes all Stops file
f.close
#opens all Lines File
d = open('Backend/jsonFiles/KVV_Lines_Stops_Based_v2.json')

lines = []
numbers = []
#gets trias numbers of lines and "name" of the line
data = json.load(d)
for item in data['lines']:
    lines.append(item['stations'])
    numbers.append(item['number'])

print(numbers)
#adds lines to the corret stations
for elements in stationlist:
    for i in range (len(lines)):
        for j in range (len(lines[i])):
            if elements.get_triasID() == lines[i][j]:
                elements.add_line(numbers[i])

for element in stationlist :
    print(element.get_name())
    print(element.get_lines())
#TODO add weights(estimated time to get from curr station to next/targt Station and weight all Stations with it)
d.close