
import eventlet
eventlet.monkey_patch()
from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import json
from package import Package
from Station  import Station
from Robot import Robot
from init_robot import init_robot
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("connect")
def handle_connect():
    print("Client connected")
    socketio.send("Welcome to the server!")
# helper Functions
def fetch_data_from_db(query, params=()):
     # Connect to the SQLite database
    conn = sqlite3.connect('simulation.db')
    cursor = conn.cursor()

    # Execute the query with optional parameters
    cursor.execute(query, params)

    # Fetch all rows from the query result
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    return rows


def fetch_one(query, params=()):
     # Connect to the SQLite database
    conn = sqlite3.connect('simulation.db')
    cursor = conn.cursor()

    # Execute the query with optional parameters
    cursor.execute(query, params)

    # Fetch all rows from the query result
    rows = cursor.fetchone()

    # Close the connection
    conn.close()

    return rows


def insert_robot(robot):
    conn = sqlite3.connect('simulation.db')
    cursor = conn.cursor()

    '''# Serialize the package_list to a JSON string
    
    position_json = json.dumps(robot.position) if isinstance(robot.position, dict) else robot.position
    dest_json = json.dumps(robot.dest) if isinstance(robot.dest, dict) else robot.dest
    start_pos_json = json.dumps(robot.start_pos) if isinstance(robot.start_pos, dict) else robot.start_pos'''
    '''package_list_json = []
    for pkg in robot.package_list:
        package = pkg.to_dict_p()
        package_list_json.append(package)'''
    package_list_json = json.dumps([package.to_dict_p() for package in robot.package_list])
    position_dict = robot.position.to_dict_s()
    dest_dict = robot.dest.to_dict_s()
    start_pos_dict = robot.start_pos.to_dict_s()
    position_json = json.dumps(position_dict)
    dest_json = json.dumps(dest_dict)
    start_pos_json = json.dumps(start_pos_dict)


    print("INSERTING WORKING")
    print(type(position_json))
    print(type(package_list_json))
    
    # Insert robot into the database
    cursor.execute('''
            INSERT INTO robots (id, position, energy, numb_packages, package_list, status, dest, speed, weight, start_pos)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (robot.id, position_json, robot.energy, robot.numb_packages, package_list_json, robot.status, dest_json, robot.speed, robot.weight, start_pos_json))  # Use placeholders to avoid SQL injection
    conn.commit()
    conn.close()

def create_robot(data):
        print("entering creating robots")
        # Get the JSON data from the request
        data = request.get_json()
        
        # Extract individual fields from the JSON data
        id = data.get('id')
         # Convert position, dest, and start_pos from dict to Station objects
        position_data = data.get('position')
        print("bnefore StaTION")
        position = Station.from_dict(position_data) if position_data else None
        print("after station")
        energy = data.get('energy')
        numb_packages = data.get('numb_packages')
        # Ensure package_list is converted to Package objects
        package_list_data = data.get('package_list', [])
        #json_package_list = json.loads(package_list_data)
        print("before package")
        package_list = [Package.from_dict(pkg) for pkg in package_list_data]  # Convert each dictionary to a Package object
        print("after pakcage")
        status = data.get('status')
        # Convert dest from dict to Station object
        dest_data = data.get('dest')
        #json_dest = json.loads(dest_data)
        dest = Station.from_dict(dest_data) if dest_data else None
        speed = data.get('speed')
        weight = data.get('weight')
        # Convert start_pos from dict to Station object
        start_pos_data = data.get('start_pos')
        #json_start_pos= json.loads(start_pos_data)
        start_pos = Station.from_dict(start_pos_data) if start_pos_data else None

        updated_robot = Robot(id=id, position=position, energy=energy, numb_packages=numb_packages, package_list=package_list, status=status, dest=dest, speed=speed, weight=weight, start_pos=start_pos)
        return updated_robot
        '''# Extract individual fields from the JSON data
        id = data.get('id')
        position = data.get('position')
        energy = data.get('energy')
        numb_packages = data.get('numb_packages')
        package_list = data.get('package_list')
        status = data.get('status')
        dest = data.get('dest')
        speed = data.get('speed')
        weight = data.get('weight')
        start_pos = data.get('start_pos')

        # Validate that required fields are provided
        required_fields = ['id', 'position', 'energy', 'numb_packages', 'package_list', 'status', 'dest', 'speed', 'weight', 'start_pos']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400
        # Convert the 'package_list' (which is a list of dictionaries) to Package objects
        package_list = [Package(p['weight'], p['width'], p['height'], p['length'], p['destination'],) for p in data['package_list']]

        # Create the Robot object
        return Robot(id=id, position=position, energy=energy, numb_packages=numb_packages, package_list=package_list, status=status, dest=dest, speed=speed, weight=weight, start_pos=start_pos)
        '''

@app.route('/config', methods=['GET'])
def get_config():
    query = 'SELECT * FROM configuration'

    # fetch data from database
    data = fetch_one(query)

    # Prepare the data in a list of dictionaries to return as JSON
    row = data

    config = {
        'numb_robots': row[0],
        'max_packages': row[1],
        'battery': row[2],
        'capacity': row[3],
        'sim_speed': row[4],
        'usage': row[5]
    }

    # Return the data as JSON
    return jsonify(config)


@app.route('/robots', methods=['GET'])
def get_robots():
    query = 'SELECT * FROM robots'

    # fetch data from database
    data = fetch_data_from_db(query)

    # Prepare the data in a list of dictionaries to return as JSON
    robots = []

    for row in data:
        robot = {
            'id': row[0],
            'position': row[1],
            'energy': row[2],
            'numb_packages': row[3],
            'package_list': row[4],
            'status': row[5],
            'dest': row[6],
            'speed': row[7],
            'weight': row[8],
            'start_pos': row[9]
        }
        robots.append(robot)

        # Return the data as JSON
    return jsonify(robots)
    

@app.route('/robot/<robot_id>', methods=['GET'])
def get_robot(robot_id):
    print("getting one robot")
    query = 'SELECT * FROM robots WHERE id = ?'

    # fetch data from database
    print(fetch_one(query, (robot_id,)))
    data = fetch_one(query, (robot_id,))
    if data is None:
        return jsonify({'error': 'Robot not found'}), 404
    # Prepare the data in a list of dictionaries to return as JSON
    
    robot = {
        'id': data[0],
        'position': json.loads(data[1]) if data[1] else [],
        'energy': data[2],
        'numb_packages': data[3],
        'package_list': json.loads(data[4]) if data[4] else [],
        'status': data[5],
        'dest': json.loads(data[6]) if data[6] else [],
        'speed': data[7],
        'weight': data[8],
        'start_pos': json.loads(data[9]) if data[9] else []
    }
    print(robot)
    robot_json = json.dumps(robot)
    print("string", robot_json)
    # Return the data as JSON
    return robot_json


@app.route('/config', methods=['POST'])
def add_config():
    # Check if the incoming request contains JSON
    if request.is_json:
        # Get JSON data from the request
        data = request.get_json()

        # Extract individual fields from the JSON data
        ''' numb_robots = data.get('numb_robots')
        max_packages = data.get('max_packages')
        battery = data.get('battery')
        capacity = data.get('capacity')
        sim_speed = data.get('sim_speed')
        usage = data.get('usage')'''
        numb_robots = data[0]
        max_packages = data[1]
        battery = data[2]
        capacity = data[3]
        sim_speed = data[4]
        usage = data[5]

        # Insert data into the SQLite database
        conn = sqlite3.connect('simulation.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO configuration (numb_robots, max_packages, battery, capacity, sim_speed, usage)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (numb_robots, max_packages, battery, capacity, sim_speed, usage))  # Use placeholders to avoid SQL injection
        conn.commit()

        # Close the connection
        conn.close()

        # Return a success message with the inserted data
        return jsonify({"message": "Configuration added successfully", "data": data}), 201
    else:
        return jsonify({"error": "Request must be in JSON format"}), 400
    

@app.route('/robots', methods=['POST'])
def add_robots():
    # Check if the incoming request contains JSON
    if request.is_json:
        # Get JSON data from the request
        data = request.get_json()
        robot = create_robot(data)
        print("creating robot works")
        # Call the insert_robot function to insert the robot into the database
        insert_robot(robot)

        # Return a success message with the inserted data
        return jsonify({"message": "Robot added successfully", "data": data}), 201
    else:
        return jsonify({"error": "Request must be in JSON format"}), 400


@app.route('/robot/<robot_id>', methods=['PATCH'])
def update_robots(robot_id):
    print("Updating the Robot with the ID: ", robot_id)
    # Check if the incoming request contains JSON
    if request.is_json:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Extract individual fields from the JSON data
        id = data.get('id')
         # Convert position, dest, and start_pos from dict to Station objects
        position_data = data.get('position')
        position = Station.from_dict(position_data) if position_data else None
        energy = data.get('energy')
        numb_packages = data.get('numb_packages')
        # Ensure package_list is converted to Package objects
        package_list_data = data.get('package_list', [])
        package_list = [Package.from_dict(pkg) for pkg in package_list_data]  # Convert each dictionary to a Package object
    
        status = data.get('status')
        # Convert dest from dict to Station object
        dest_data = data.get('dest')
        dest = Station.from_dict(dest_data) if dest_data else None
        speed = data.get('speed')
        weight = data.get('weight')
        # Convert start_pos from dict to Station object
        start_pos_data = data.get('start_pos')
        start_pos = Station.from_dict(start_pos_data) if start_pos_data else None

        # Now serialize position, dest, and start_pos to strings (if they are objects)
        position_json = json.dumps(position.to_dict_s()) if position else None
        dest_json = json.dumps(dest.to_dict_s()) if dest else None
        start_pos_json = json.dumps(start_pos.to_dict_s()) if start_pos else None

        updated_robot = Robot(id=id, position=position, energy=energy, numb_packages=numb_packages, package_list=package_list, status=status, dest=dest, speed=speed, weight=weight, start_pos=start_pos)
       
        dict_robot = updated_robot.to_dict()
        
        # Validate that required fields are provided
        required_fields = ['id', 'position', 'energy', 'numb_packages', 'package_list', 'status', 'dest', 'speed', 'weight', 'start_pos']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400
        # Convert the 'package_list' (which is a list of dictionaries) to Package objects
        #package_list = [Package(p['weight'], p['width'], p['height'], p['length'], p['destination'],) for p in data['package_list']]
        # Serialize the package_list to a JSON string
        package_list_json = json.dumps([package.to_dict_p() for package in package_list])
        data["package_list"] = package_list_json


        # Build the update query based on the provided data
        updates = []
        parameters = []
        emit_data = []

        # Only update fields that are provided in the request
        # Only update fields that are provided in the request
        for field in required_fields:
            if field in data:
                if field == 'package_list':
                    updates.append(f"{field} = ?")  # We set package_list to JSON
                    parameters.append(package_list_json)
                    emit_data.append(package_list_json)
                elif field == 'position':
                    updates.append(f"{field} = ?")  # We set position to serialized JSON
                    parameters.append(position_json)
                    emit_data.append(position_json)
                elif field == 'dest':
                    updates.append(f"{field} = ?")  # We set dest to serialized JSON
                    parameters.append(dest_json)
                    emit_data.append(dest_json)
                elif field == 'start_pos':
                    updates.append(f"{field} = ?")  # We set start_pos to serialized JSON
                    parameters.append(start_pos_json)
                    emit_data.append(start_pos_json)
                else:
                    updates.append(f"{field} = ?")
                    parameters.append(data[field])
                    emit_data.append(data[field])

        # Add the condition to update the robot by its id
        updates_query = ', '.join(updates)
        parameters.append(robot_id)

        conn = sqlite3.connect('simulation.db')
        cursor = conn.cursor()

        print("got till here")
        # Insert robot into the database
        cursor.execute(f'UPDATE robots SET {updates_query} WHERE id = ?', parameters)  # Use placeholders to avoid SQL injection
        conn.commit()
        conn.close()

        # Emit a message to all connected clients
        print("before emit")
        socketio.emit('robot_updated', emit_data)
        print("after emit")

        #update_robot(robot,updates_query, parameters)
        # Execute the update query

        # Return the updated product data
        return jsonify({
            "message": "Product updated successfully",
            "data": data
        }), 200

    else:
        return jsonify({"error": "Request must be in JSON format"}), 400


@app.route('/config', methods=['PATCH'])
def update_config():

    # Check if the incoming request contains JSON
    if request.is_json:
        # Get the JSON data from the request
        data = request.get_json()

        # Define required fields
        required_fields = ['numb_robots', 'max_packages', 'battery', 'capacity', 'sim_speed', 'usage']

        # Check if all the required fields are present in the request
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Establish database connection
        conn = sqlite3.connect('simulation.db')
        cursor = conn.cursor()

        # Build the update query based on the provided data
        updates = []
        parameters = []

        # Only update fields that are provided in the request
        for field in required_fields:
            if field in data:
                updates.append(f"{field} = ?")
                parameters.append(data[field])

        # Since this is a single row, we don't need to filter by id in the WHERE clause,
        # but we assume the row has an ID of 1 for simplicity.
        updates_query = ', '.join(updates)

        # Execute the update query for the single row
        cursor.execute(f'UPDATE configuration SET {updates_query} WHERE id = 1', parameters)
        conn.commit()

        # Check if any rows were updated
        if cursor.rowcount == 0:
            return jsonify({"error": "No rows were updated"}), 404

        # Close the database connection
        conn.close()

        # Return the updated settings data
        return jsonify({
            "message": "Configuration updated successfully",
            "data": data
        }), 200

    else:
        return jsonify({"error": "Request must be in JSON format"}), 400

@app.route('/config/delete', methods=['DELETE'])
def config_delete():
    try:
        # Establish connection to the SQLite database
        conn = sqlite3.connect('simulation.db')
        cursor = conn.cursor()

        # SQL query to delete all records from the table (e.g., "items")
        cursor.execute("DELETE FROM configuration")
        
        # Commit the changes
        conn.commit()
        
        # Close the connection
        conn.close()

        return jsonify({"message": "All data deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"message": "Error deleting data", "error": str(e)}), 500

@app.route('/robots/delete', methods=['DELETE'])
def robot_delete():
    try:
        # Establish connection to the SQLite database
        conn = sqlite3.connect('simulation.db')
        cursor = conn.cursor()

        # SQL query to delete all records from the table (e.g., "items")
        cursor.execute("DELETE FROM robots")
        
        # Commit the changes
        conn.commit()
        
        # Close the connection
        conn.close()

        return jsonify({"message": "All data deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"message": "Error deleting data", "error": str(e)}), 500

# Robot Methods

@app.route('/robot/charge', methods=['POST'])
def charge_robot():
    if request.is_json:
        # Get JSON data from the request
        data = request.get_json()
        robot = create_robot(data)
        print("------------------------")
        robot.charge()

@app.route('/robot/wait', methods=['POST'])
def wait_robot():
    print("here")
    if request.is_json:
        print("cirrect")
        # Get JSON data from the request
        data = request.get_json()
        robot = create_robot(data)
        robot.waitForNextTram()

@app.route('/robot/deliever', methods=['POST'])
def deliever_robot():
    if request.is_json:
        # Get JSON data from the request
        data = request.get_json()
        robot = create_robot(data)
        robot.delieverPackage()

@app.route('/robot/load', methods=['POST'])
def load_robot():
    if request.is_json:
        # Get JSON data from the request
        data = request.get_json()
        robot = create_robot(data)
        robot.loadPackage()

# Statin methods
@app.route('/stations', methods=['GET'])
def get_all_stations():
    query = 'SELECT * FROM stations'

    # fetch data from database
    data = fetch_data_from_db(query)

    # Prepare the data in a list of dictionaries to return as JSON
    stations = []

    for row in data:
        station = {
            'name': row[0],
            'trias_id': row[1],
            'lines': row[2],
            'lat': row[3],
            'long': row[4],
            'connections': row[5]
        }
        stations.append(station)

        # Return the data as JSON
    return jsonify(stations)

@app.route('/station/<trias_id>', methods=['GET'])
def get_station(trias_id):
    print("getting one  station")
    query = 'SELECT * FROM stations WHERE trias_id = ?'

    # fetch data from database
    print(fetch_one(query, (trias_id,)))
    data = fetch_one(query, (trias_id,))
    if data is None:
        return jsonify({'error': 'Robot not found'}), 404
    # Prepare the data in a list of dictionaries to return as JSON
    
    station = {
        'name': data[0],
        'trias_id': data[1],
        'lines': json.loads(data[2]) if data[2] else [],
        'lat': data[3],
        'long': data[4],
        'connections': json.loads(data[5]) if data[5] else []
    }
    print(station)
    station_json = json.dumps(station)
    print("string", station_json)
    # Return the data as JSON
    return station_json

# Simulation methods

@app.route('/start_sim', methods=['POST'])
def start_sim():
    if request.is_json:
        print("if")
        # Get JSON data from the request
        data = request.get_json()
        numb_robots = data['numb_robots']
        max_packages = data['max_packages']
        battery = data['battery']
        init_robot.init_robot(numb_robots, max_packages, battery)
        return ("it works")


if __name__ == '__main__':
    #app.run(debug=True)
    socketio.run(app, debug=True)