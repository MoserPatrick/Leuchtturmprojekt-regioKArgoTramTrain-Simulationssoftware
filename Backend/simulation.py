from Robot import Robot
from package import Package
from create_package import package_creator
import requests
import json
import sqlite3
from Station import Station
from jsonreader import jsonreader as jread




class Simulation:
    
    def main():
        connection = sqlite3.connect('simulation.db')
        cursor = connection.cursor()

        stationlist = []
        numbers = ['1', '2', '3', '4', '5', '8', '17', '18', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S11', 'S12', 'S31', 'S32', 'S33', 'S51', 'S52', 'S71', 'S81']
        # Lade alle Daten aus der stations-Tabelle
        for table_name in numbers:
            query = f'SELECT name, trias_id, lines, lat, long FROM "line_{table_name}"'
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                name, trias_id, lines_json, lat, long = row
                lines = json.loads(lines_json)  # Konvertiere das JSON-String zurück in ein Array
                station = Station(name, trias_id, lat, long)
                for line in lines:
                    station.add_line(line)
                stationlist.append(station)
        connection.close()
        trias_id_list, numbers = jread.get_lines_and_stations()
        jread.add_lines_to_stations(stationlist, trias_id_list, numbers)
        sorted_stationlist = jread.sort_stationlist(stationlist, trias_id_list)
        jread.calculate_weight_and_create_connections(sorted_stationlist, numbers)
        inverted_sorted_stationlist = []
        for i in range (len(sorted_stationlist)):
                inverted_sorted_stationlist.append(sorted_stationlist[i][::-1])
        jread.calculate_weight_and_create_connections(inverted_sorted_stationlist, numbers)
        

            
        # HELPING CODE
        # example for getting Robot from Database
        robot_id = 1
        url_get_robot = f"http://127.0.0.1:5000/robot/{robot_id}"
        response = requests.get(url_get_robot)
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
        else:
            obj_robot = json.loads(response.text)
            robot = Robot.from_dict(obj_robot)
            #robot.charge()




        '''for i in range(numb_robots):
            # Create package_list
            package_list = []    
            # creating packages 
            package_list = package_creator.create_package(max_packages, package_list)
            
            robot = Robot(i+1, pos, energy, max_packages, package_list, status, dest, speed, weight)
            json_robot = robot.to_dict()
            response = requests.post(url, json= json_robot)

            # Check the response from the server
            if response.status_code == 201:  # 201 Created
                print("Data successfully posted!")
                print("Server Response:", response.json())
            else:
                print(f"Error: Received status code {response.status_code}")
                print("Message:", response.text)

            robots.append(robot)'''


        #robot.charge()

        pass

    if __name__ == "__main__":
        main()