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
    weight REAL)
    """
cursor.execute(command2)
# add to config
cursor.execute("INSERT INTO configuration VALUES (3, 3, 100.0, 100.0, 75.5, 1.0)")
cursor.execute("INSERT INTO robots VALUES (1, 'yes', 100.0, 2, 'packages', 'waiting', 'here', 1.0, 100.0)")
connection.commit()

cursor.execute("SELECT * FROM configuration")
cursor.execute("SELECT * FROM robots")

results = cursor.fetchall()
cursor.close()
connection.close()
print(results)