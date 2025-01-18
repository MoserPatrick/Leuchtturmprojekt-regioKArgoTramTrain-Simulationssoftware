import json
import Station
from harversine import haversine

stationlist = []
names = []
trias_id = []
lat = []
long = []
coordinates = []
#opens KVV Stops File
f = open('Backend/jsonFiles/KVV_Stops_v4.json')
data = json.load(f)
for item in data:
    names.append(item['name'])
    trias_id.append(item['triasID'])
    #print(item['triasID'])
    # test if key "coordPositionWGS84" exist
    if "coordPositionWGS84" in item:
        coordinates.append({
            "lat": item["coordPositionWGS84"].get("lat", None),  
            "long": item["coordPositionWGS84"].get("long", None) 
        })
    else:
        print(f"Warnung: 'coordPositionWGS84' fehlt bei der Station {item.get('name', 'Unbekannt')}")
for i in range(len(names)):
    #print(trias_id[i])
    stationlist.append(Station.Station(names[i], trias_id[i], coordinates[i]["lat"], coordinates[i]["long"]))


    
#closes all Stops file
f.close
#opens all Lines File
d = open('Backend/jsonFiles/KVV_Lines_Stops_Based_v2.json')
#[[de:2314]]
trias_id_list = []
numbers = []
#gets trias numbers of lines and "name" of the line
data = json.load(d)
for item in data['lines']:
    #print(item['stations'])
    trias_id_list.append(item['stations'])
    numbers.append(item['number'])

print(numbers)
#adds lines to the corret stations
for element in stationlist:

    for i in range (len(trias_id_list)):

        for j in range (len(trias_id_list[i])):

            if element.get_triasID() == trias_id_list[i][j]:

                #print(trias_id_list[i][j])

                #print(element.get_triasID()+)

                element.add_line(numbers[i])
            


                
stationlist_without_busstops = []

for elements in stationlist:
    if elements.lines != []:
        stationlist_without_busstops.append(elements)



d.close

'''for element in stationlist :
    print(element.get_name())
    print(element.get_lines())
    print(element.get_lat())
    print(element.get_long())
    print(element.get_triasID()+"\n")'''

"""for element in stationlist_without_busstops:
    if len(element.get_lines()) > 1:
        print(element.get_name())
        print(type(element.get_triasID()))"""

"""linien rauslesen 
haltestelen separieren in andere liste
ordnen nach kvv stops tris id
mit koordinaten gewicht für dikstra berechnen

(für linien)


mit straßenübergang
-> vorschlag : 1-5 min randomizer zusätzlich zu gewicht
"""

sorted_stationlist = trias_id_list
for i in range (len(trias_id_list)):
    for j in range (len(trias_id_list[i])):
        for element in stationlist:
            if element.get_triasID() == trias_id_list[i][j]:
                sorted_stationlist[i][j] = element


'''for list in sorted_stationlist:
    print("---------------------------------------------------------------------------------")
    for element in list:
        print(element.get_name())
'''
            
# Beispiel-Koordinaten
lat1, lon1 = 49.0019896339322, 8.45542854438636  
lat2, lon2 = 49.0363295015307, 8.38806388123024   

# Berechnung
sum = 0
lat1 = 0
long1 = 0
lat2 = 0
long2 = 0
for i in range (len(sorted_stationlist)):
    for j in range(len(sorted_stationlist[i])-1):
        lat1 = float(sorted_stationlist[i][j].get_lat())
        long1 = float(sorted_stationlist[i][j].get_long())
        lat2 = float(sorted_stationlist[i][j+1].get_lat())
        long2 = float(sorted_stationlist[i][j+1].get_long())
        #print(sorted_stationlist[i][j].get_name())
        #print(lat1,long1)
        #print("\n")
        #print(sorted_stationlist[i][j+1].get_name())
        #print(lat2,long2)
        
        distance = haversine(lat1, long1, lat2, long2)
        #print(f"Die Distanz zwischen den Punkten beträgt: {distance:.2f} km")
        time = 0
        if i <= 7:
            #Straßenbahn
            geschw = 19.8
            time = distance/geschw*60
        else:
            #Stadtbahn
            geschw = 30
            time = distance/geschw*60
        sorted_stationlist[i][j].add_connection(sorted_stationlist[i][j+1], time, numbers[i])
        #print(sorted_stationlist[i][j].get_connection())
        #for h in range (len(sorted_stationlist[i][j].get_connection())):
            #print (sorted_stationlist[i][j].get_connection()[h][0].get_name())
        #print("---------------------------------------------------------")
        sum = sum + distance
    #print(sum)





inverted_sorted_stationlist = []
for i in range (len(sorted_stationlist)):
    inverted_sorted_stationlist.append(sorted_stationlist[i][::-1])
    

for i in range (len(inverted_sorted_stationlist)):
    for j in range(len(inverted_sorted_stationlist[i])-1):
        lat1 = float(inverted_sorted_stationlist[i][j].get_lat())
        long1 = float(inverted_sorted_stationlist[i][j].get_long())
        lat2 = float(inverted_sorted_stationlist[i][j+1].get_lat())
        long2 = float(inverted_sorted_stationlist[i][j+1].get_long())
        print(inverted_sorted_stationlist[i][j].get_name())
        #print(lat1,long1)
        #print("\n")
        #print(inverted_sorted_stationlist[i][j+1].get_name())
        #print(lat2,long2)
        distance = haversine(lat1, long1, lat2, long2)
        #print(f"Die Distanz zwischen den Punkten beträgt: {distance:.2f} km")    
        time = 0
        if i <= 7:
            #Straßenbahn
            geschw = 19.8
            time = distance/geschw*60
        else:
            #Stadtbahn
            geschw = 30
            time = distance/geschw*60


        inverted_sorted_stationlist[i][j].add_connection(inverted_sorted_stationlist[i][j+1], time, numbers[i])
        print(inverted_sorted_stationlist[i][j].get_connection())
        for h in range (len(inverted_sorted_stationlist[i][j].get_connection())):
            print (inverted_sorted_stationlist[i][j].get_connection()[h][0].get_name())
        print("----------------------------------------")
    sum = sum + distance

#19,8 km/h straßenbahnm 0-7
#30 km/h stadtbahnen 8-17
                

