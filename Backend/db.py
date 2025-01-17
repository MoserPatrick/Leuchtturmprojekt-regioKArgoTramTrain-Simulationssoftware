import sqlite3

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
    trias_id INT,
    lines TEXT,
    lat REAL,
    long REAL,
    connections TEXT)
"""

cursor.execute(command3)
# add to config
#cursor.execute("INSERT INTO configuration VALUES (3, 3, 100.0, 100.0, 75.5, 1.0)")
#cursor.execute("INSERT INTO robots VALUES (1, 'yes', 100.0, 2, 'packages', 'waiting', 'here', 1.0, 100.0, 'start')")
cursor.execute("INSERT INTO stations VALUES ('name', 123, 'lines', 1.1, 2.2, 'connections')")
cursor.execute("INSERT INTO stations VALUES ('name2', 123, 'lines', 1.1, 2.2, 'connections')")
connection.commit()

cursor.execute("SELECT * FROM configuration")
cursor.execute("SELECT * FROM robots")
cursor.execute("SELECT * FROM stations")

results = cursor.fetchall()
cursor.close()
connection.close()
print(results)