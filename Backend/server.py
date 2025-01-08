from flask import Flask, send_from_directory, jsonify, request
import os
import json

#from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = 'localhost'

app = Flask(__name__)

# File names
DATA_FILE_CONFIG = 'config_data.json'

# helper Functions


# Loading the pages
# Default page
@app.route('/')
def index():
    return 'hello world'

# Configuration Page
@app.route('/config')
def configuration():
    fronend_path = os.path.join(app.root_path, '..', 'Frontend', 'Configuration_page')
    return send_from_directory(fronend_path, 'config.html')

# Simulation Page
@app.route('/simulation')
def simulation():
    fronend_path = os.path.join(app.root_path, '..', 'Frontend', 'Simulation_page')
    return send_from_directory(fronend_path, 'simulation.html')

# GET Configuration data
@app.route('api/data/config', methods=['GET'])
def get_data_config():
    with open(DATA_FILE_CONFIG, 'r') as file:
        data = json.load(file)
    return jsonify(data)

# PATCH Configuration Data
@app.route('/api/echo/config', methods=['PATCH'])
def echo_data_config():
    input_data = request.json
    # Step 1: Read the existing data
    with open(DATA_FILE_CONFIG, 'r') as file:
        data = json.load(file)

    # Step 2: Remove the entry
    data = [entry for entry in data if entry["Name"] != "Charlie"]  # Keep all except Charlie

    # Step 3: Write the updated data back to the file
    with open(DATA_FILE_CONFIG, 'w') as file:
        json.dump(data, file, indent=4)

    return jsonify({
        "message": "Daten empfangen",
        "data": input_data
    })


if __name__ == '__main__':
    app.run(debug=True)


'''class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/Frontend/Configuration_page/config.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # post something

        self.wfile.write(bytes('{"time": "' + 100 + '"\}', "utf-8"))



httpd = HTTPServer((HOST, PORT), Serv)
httpd.serve_forever()'''

# Quick copy page links
# http://127.0.0.1:5500/Frontend/Configuration_page/config.html
# http://127.0.0.1:5500/Frontend/Simulation_page/simulation.html