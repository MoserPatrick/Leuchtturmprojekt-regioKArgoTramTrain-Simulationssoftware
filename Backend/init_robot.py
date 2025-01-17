from create_package import package_creator
import requests
from Robot import Robot
import random

class init_robot:

    def init_robot(numb_robots, max_packages, battery):

        url_get_stations = "http://127.0.0.1:5000/stations"
        response_stations = requests.get(url_get_stations)
        stations = response_stations.json()
        

        # Select two random stations
        start_pos = random.choice(stations)
        
        # Remove the first selected station from the list to avoid duplicate selection
        remaining_stations = [station for station in stations if station != start_pos]
        dest = random.choice(remaining_stations)

        pos = start_pos
        status = "delivering"
        weight = 0.0 #TODO
        speed = 0.0
        url = "http://127.0.0.1:5000/robots"
        for i in range(int(numb_robots)):
            package_list = []
            #creating packages-----------------------------------------------
            package_list = package_creator.create_package(max_packages, package_list, pos)
            for package in package_list:
                weight += package.weight
                speed = 2 - (weight/100)
            print("create Robot object")
            robot = Robot(i+1, pos, battery, max_packages, package_list, status, dest, speed, weight, start_pos)
            print("finished creating Robot")
            json_robot = robot.to_dict()
            response = requests.post(url, json=json_robot)

            # checking for error
            if response.status_code ==201:
                print("data successfully posted!")
                print("Server Response: ", response.json())
            else:
                print(f"Error: Received status code {response.status_code}")
                print("Message:", response.text)