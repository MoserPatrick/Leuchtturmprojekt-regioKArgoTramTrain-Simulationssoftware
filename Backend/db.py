import sqlite3
import json

linien_list =['1', '2', '3', '4', '5', '8', '17', '18', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S11', 'S12', 'S31', 'S32', 'S33', 'S51', 'S52', 'S71', 'S81']

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

command3 ="""
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
"""
i = 0
for element in linien_list:
    command5= """
    CREATE TABLE IF NOT EXISTS{element}(
    station TEXT
    )
    """
cursor.execute(command3)
# add to config
#cursor.execute("INSERT INTO configuration VALUES (3, 3, 100.0, 100.0, 75.5, 1.0)")
#cursor.execute("INSERT INTO robots VALUES (1, 'yes', 100.0, 2, 'packages', 'waiting', 'here', 1.0, 100.0, 'start')")
lines = ["line3", "line4"]
connections = [['station1', 'station2'], ['station3', 'station4'], ['station5']]
lines_json = json.dumps(lines)  # Convert lines list to a JSON string
connections_json = json.dumps(connections)  # Convert 2D list to a JSON string
cursor.execute("INSERT INTO stations VALUES ('name', '123', ?, 1.1, 2.2)", (lines_json))
cursor.execute("INSERT INTO stations VALUES ('name2', '123', ?, 1.1, 2.2)", (lines_json))



connection.commit()

cursor.execute("SELECT * FROM configuration")
cursor.execute("SELECT * FROM robots")
cursor.execute("SELECT * FROM stations")

results = cursor.fetchall()
cursor.close()
connection.close()
print(results)