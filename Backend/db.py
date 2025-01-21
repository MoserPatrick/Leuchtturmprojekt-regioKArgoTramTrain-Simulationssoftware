import sqlite3
import json
from jsonreader import jsonreader as jread


stationlist = jread.create_stationlist()
trias_id_list, numbers = jread.get_lines_and_stations()
jread.add_lines_to_stations(stationlist, trias_id_list, numbers)
sorted_stationlist = jread.sort_stationlist(stationlist, trias_id_list)
'''jread.calculate_weight_and_create_connections(sorted_stationlist, numbers)
inverted_sorted_stationlist = []
for i in range (len(sorted_stationlist)):
        inverted_sorted_stationlist.append(sorted_stationlist[i][::-1])
jread.calculate_weight_and_create_connections(inverted_sorted_stationlist, numbers)'''

print(numbers)

'''for element in stationlist:
        print(element.get_name())
        print(type(element.get_name()))
        print(element.get_lines())
        print(element.get_long())
        print(element.get_lat())
        print(element.get_connection())'''

#define connection and cursor
connection = sqlite3.connect('simulation.db')

cursor = connection.cursor()

# create tables
command1 = """
CREATE TABLE IF NOT EXISTS configuration (
    numb_robots INT,
    max_packages INT,
    battery REAL,
    capacity REAL,
    sim_speed REAL,
    usage REAL)
    """
cursor.execute(command1)

command2 = """
CREATE TABLE IF NOT EXISTS robots (
    id INT,
    position TEXT,
    energy REAL,
    numb_packages INT,
    package_list TEXT,
    status TEXT,
    dest TEXT,
    speed REAL,
    weight REAL,
    start_pos TEXT)
    """

cursor.execute(command2)

'''command3 ="""
CREATE TABLE IF NOT EXISTS stations(
    name TEXT,
    trias_id TEXT,
    lines TEXT,
    lat REAL,
    long REAL)
"""

command4 ="""
CREATE TABLE IF NOT EXISTS lines(
    name TEXT,
    trias_id TEXT,
    lines TEXT,
    lat REAL,
    long REAL)
"""'''
test = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","huan"]
for table_name in numbers:
    command3 = f'''
    CREATE TABLE IF NOT EXISTS "line_{table_name}" (
        name TEXT,
        trias_id TEXT,
        lines TEXT,
        lat REAL,
        long REAL)
    '''
    cursor.execute(command3)

for i in range(len(sorted_stationlist)):
    for j in range(len(sorted_stationlist[i])):
        name = sorted_stationlist[i][j].get_name()
        trias_id = sorted_stationlist[i][j].get_triasID()
        lines = json.dumps(sorted_stationlist[i][j].get_lines())
        lat = sorted_stationlist[i][j].get_lat()
        long = sorted_stationlist[i][j].get_long()
        table_name = numbers[i]
        query = f'INSERT INTO "line_{table_name}" (name, trias_id, lines, lat, long) VALUES (?, ?, ?, ?, ?)'
        #cursor.execute("INSERT INTO {table_name} (name, trias_id, lines, lat, long) VALUES (?, ?, ?, ?, ?)", (name,trias_id,lines,lat,long))
        cursor.execute(query, (name, trias_id, lines, lat, long))


'''cursor.execute(command3)
# add to config
#cursor.execute("INSERT INTO configuration VALUES (3, 3, 100.0, 100.0, 75.5, 1.0)")
#cursor.execute("INSERT INTO robots VALUES (1, 'yes', 100.0, 2, 'packages', 'waiting', 'here', 1.0, 100.0, 'start')")
lines = numbers
#connections = [['station1', 'station2'], ['station3', 'station4'], ['station5']]
lines_json = json.dumps(lines)  # Convert lines list to a JSON string
connections_json = json.dumps(connections)  # Convert 2D list to a JSON string
cursor.execute("INSERT INTO stations VALUES ('name', '123', ?, 1.1, 2.2)", (lines_json))
cursor.execute("INSERT INTO stations VALUES ('name2', '123', ?, 1.1, 2.2)", (lines_json))'''



connection.commit()

cursor.execute("SELECT * FROM configuration")
cursor.execute("SELECT * FROM robots")
cursor.execute("SELECT * FROM stations")

results = cursor.fetchall()
cursor.close()
connection.close()
print(results)