from flask import Flask, jsonify, request
import sqlite3
import json
from package import Package
from Robot import Robot

app = Flask(__name__)

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

def insert_robot(robot):
    conn = sqlite3.connect('simulation.db')
    cursor = conn.cursor()

    # Serialize the package_list to a JSON string
    package_list_json = json.dumps([package.to_dict() for package in robot.package_list])

    # Insert robot into the database
    cursor.execute('''
            INSERT INTO robots (id, position, energy, numb_packages, package_list, status, dest, speed, weight)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (robot.id, robot.position, robot.energy, robot.numb_packages, package_list_json, robot.status, robot.dest, robot.speed, robot.weight))  # Use placeholders to avoid SQL injection
    conn.commit()
    conn.close()

@app.route('/config', methods=['GET'])
def get_config():
    query = 'SELECT * FROM configuration'

    # fetch data from database
    data = fetch_data_from_db(query)

    # Prepare the data in a list of dictionaries to return as JSON
    row = data[0]

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
            'energy': row(2),
            'numb_packages': row[3],
            'package_list': row[4],
            'status': row[5],
            'dest': row[6],
            'speed': row[7],
            'weight': row[8]
        }
        robots.append(robot)

        # Return the data as JSON
        return jsonify(robots)


@app.route('/config', methods=['POST'])
def add_config():
    # Check if the incoming request contains JSON
    if request.is_json:
        # Get JSON data from the request
        data = request.get_json()

        # Extract individual fields from the JSON data
        numb_robots = data.get('numb_robots')
        max_packages = data.get('max_packages')
        battery = data.get('battery')
        capacity = data.get('capacity')
        sim_speed = data.get('max_packages')
        usage = data.get('usage')

        # Validate that required fields are provided
        required_fields = ['numb_robots', 'max_packages', 'battery', 'capacity', 'sim_speed', 'usage']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

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

        # Extract individual fields from the JSON data
        id = data.get('id')
        position = data.get('position')
        energy = data.get('energy')
        numb_packages = data.get('numb_packages')
        package_list = data.get('package_list')
        status = data.get('status')
        dest = data.get('dest')
        speed = data.get('speed')
        weight = data.get('weight')

        # Validate that required fields are provided
        required_fields = ['id', 'position', 'energy', 'numb_packages', 'package_list', 'status', 'dest', 'speed', 'weight']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400
        # Convert the 'package_list' (which is a list of dictionaries) to Package objects
        package_list = [Package(p['weight'], p['width'], p['height'], p['length'], p['destination'],) for p in data['package_list']]

        # Create the Robot object
        robot = Robot(id=id, position=position, energy=energy, numb_packages=numb_packages, package_list=package_list, status=status, dest=dest, speed=speed, weight=weight)

        # Call the insert_robot function to insert the robot into the database
        insert_robot(robot)

        # Insert data into the SQLite database
        #conn = sqlite3.connect('simulation.db')
        #cursor = conn.cursor()
        #cursor.execute('''
        #    INSERT INTO robots (id, position, energy, numb_packages, package_list, status, dest, speed, weight)
        #    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        #''', (id, position, energy, numb_packages, package_list, status, dest, speed, weight))  # Use placeholders to avoid SQL injection
        #conn.commit()

        # Close the connection
        #conn.close()

        # Return a success message with the inserted data
        return jsonify({"message": "Robot added successfully", "data": data}), 201
    else:
        return jsonify({"error": "Request must be in JSON format"}), 400


@app.route('/robots/<robot_id>', methods=['PATCH'])
def update_robots(robot_id):
    # Check if the incoming request contains JSON
    if request.is_json:
        # Get the JSON data from the request
        data = request.get_json()

        # Define required fields
        required_fields = ['id', 'position', 'energy', 'numb_packages', 'package_list', 'status', 'dest', 'speed', 'weight']

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

        # Add the condition to update the robot by its id
        updates_query = ', '.join(updates)
        parameters.append(robot_id)

        # Execute the update query
        cursor.execute(f'UPDATE robots SET {updates_query} WHERE id = ?', parameters)
        conn.commit()

        # Check if any rows were updated
        if cursor.rowcount == 0:
            return jsonify({"error": "Robot not found"}), 404

        # Close the database connection
        conn.close()

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


if __name__ == '__main__':
    app.run(debug=True)