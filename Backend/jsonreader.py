import json
import Station

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
    # test if key "coordPositionWGS84" exist
    if "coordPositionWGS84" in item:
        coordinates.append({
            "lat": item["coordPositionWGS84"].get("lat", None),  
            "long": item["coordPositionWGS84"].get("long", None) 
        })
    else:
        print(f"Warnung: 'coordPositionWGS84' fehlt bei der Station {item.get('name', 'Unbekannt')}")
for i in range(len(names)):
    stationlist.append(Station.Station(names[i], trias_id[i], coordinates[i]["lat"], coordinates[i]["long"]))


    
#closes all Stops file
f.close
#opens all Lines File
d = open('Backend/jsonFiles/KVV_Lines_Stops_Based_v2.json')

trias_id_list = []
numbers = []
#gets trias numbers of lines and "name" of the line
data = json.load(d)
for item in data['lines']:
    trias_id_list.append(item['stations'])
    numbers.append(item['number'])

print(numbers)
#adds lines to the corret stations
for elements in stationlist:
    for i in range (len(trias_id_list)):
        for j in range (len(trias_id_list[i])):
            if elements.get_triasID() == trias_id_list[i][j]:
                elements.add_line(numbers[i])
                
stationlist_without_busstops = []

for elements in stationlist:
    if elements.lines != []:
        stationlist_without_busstops.append(elements)




d.close

'''for element in stationlist_without_busstops :
    print(element.get_name())
    print(element.get_lines())
    print(element.get_lat())
    print(element.get_long())
    print(element.get_triasID())'''

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

stationlist_line_1 = []
stationlist_line_2 = []
stationlist_line_3 = []
stationlist_line_4 = []
stationlist_line_5 = []
stationlist_line_8 = []
stationlist_line_17 = []
stationlist_line_18 = []
stationlist_line_S1 = []
stationlist_line_S2 = []
stationlist_line_S3 = []
stationlist_line_S4 = []
stationlist_line_S5 = []
stationlist_line_S6 = []
stationlist_line_S7 = []
stationlist_line_S8 = []
stationlist_line_S9 = []
stationlist_line_S11 = []
stationlist_line_S12 = []
stationlist_line_S32 = []
stationlist_line_S33 = []
stationlist_line_S52 = []
stationlist_line_S71 = []
stationlist_line_S81 = []

for element in stationlist_without_busstops:
    match element.get_lines():
        case trias_id_list if "1" in trias_id_list:
            stationlist_line_1.append(element)
        case trias_id_list if "2" in trias_id_list:
            stationlist_line_2.append(element)
        case trias_id_list if "3" in trias_id_list:
            stationlist_line_3.append(element)
        case trias_id_list if "4" in trias_id_list:
            stationlist_line_4.append(element)
        case trias_id_list if "5" in trias_id_list:
            stationlist_line_5.append(element)
        case trias_id_list if "8" in trias_id_list:
            stationlist_line_8.append(element)
        case trias_id_list if "17" in trias_id_list:
            stationlist_line_17.append(element)
        case trias_id_list if "18" in trias_id_list:
            stationlist_line_18.append(element)
        case trias_id_list if "S1" in trias_id_list:
            stationlist_line_S1.append(element)
        case trias_id_list if "S2" in trias_id_list:
            stationlist_line_S2.append(element)
        case trias_id_list if "S3" in trias_id_list:
            stationlist_line_S3.append(element)
        case trias_id_list if "S4" in trias_id_list:
            stationlist_line_S4.append(element)
        case trias_id_list if "S5" in trias_id_list:
            stationlist_line_S5.append(element)
        case trias_id_list if "S6" in trias_id_list:
            stationlist_line_S6.append(element)
        case trias_id_list if "S7" in trias_id_list:
            stationlist_line_S7.append(element)
        case trias_id_list if "S8" in trias_id_list:
            stationlist_line_S8.append(element)
        case trias_id_list if "S9" in trias_id_list:
            stationlist_line_S9.append(element)
        case trias_id_list if "S11" in trias_id_list:
            stationlist_line_S11.append(element)
        case trias_id_list if "S12" in trias_id_list:
            stationlist_line_S12.append(element)
        case trias_id_list if "S32" in trias_id_list:
            stationlist_line_S32.append(element)
        case trias_id_list if "S33" in trias_id_list:
            stationlist_line_S33.append(element)
        case trias_id_list if "S52" in trias_id_list:
            stationlist_line_S52.append(element)
        case trias_id_list if "S71" in trias_id_list:
            stationlist_line_S71.append(element)
        case trias_id_list if "S81" in trias_id_list:
            stationlist_line_S81.append(element)

"""for element in stationlist_line_1:
    print(element.get_name())"""


stationlist_line_2 = []
stationlist_line_3 = []
stationlist_line_4 = []
stationlist_line_5 = []
stationlist_line_8 = []
stationlist_line_17 = []
stationlist_line_18 = []
stationlist_line_S1 = []
stationlist_line_S2 = []
stationlist_line_S3 = []
stationlist_line_S4 = []
stationlist_line_S5 = []
stationlist_line_S6 = []
stationlist_line_S7 = []
stationlist_line_S8 = []
stationlist_line_S9 = []
stationlist_line_S11 = []
stationlist_line_S12 = []
stationlist_line_S32 = []
stationlist_line_S33 = []
stationlist_line_S52 = []
stationlist_line_S71 = []
stationlist_line_S81 = []

sorted_stationlist_line_1 = []


#TODO die linien müssen sortiert werden nach dem kvv lines stops based trias ids 
#danach berechnen von gewichten anhand entfernung also meter und wie lang man dafür braucht
#zusätzlich gewichte anpassen mit vll randomizer an den umstiegspunkten

""""for i in range(len(trias_id_list)):
    for j in range(len(trias_id_list[i])):
        for element in stationlist_line_1:
            if trias_id_list[i][j] == element.get_triasID():
                sorted_stationlist_line_1.append(element)
                print(element.get_name())"""


"""for element in sorted_stationlist_line_1:
    print(element.get_name())"""

            

                

