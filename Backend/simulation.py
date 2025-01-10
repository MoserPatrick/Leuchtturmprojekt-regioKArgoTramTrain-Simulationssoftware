from Robot import Robot
from package import Package
from create_package import package_creator
import requests
import json


class Simulation:

    def main():

        url_get_config = f"http://127.0.0.1:5000/config"
        response_config = requests.get(url_get_config)
        config = json.loads(response_config.text)
        
        # Create Robots
        # Configurated Data 
        numb_robots = config['numb_robots'] # LOAD: load the config data
        max_packages = config['max_packages'] # LOAD: load the config number of Packages
        battery = config['battery']
        capacity = config['capacity']
        sim_speed = config['sim_speed']
        usage = config['usage']

        # Robot Data
        pos = "(100, 50)" # LOAD: load the real starting Position (Station)
        energy = battery # LOAD: from config
        numb_packages = max_packages
        package_list = []
        status = "idle"
        dest = "Station"
        weight = 80.0 # LOAD: load form config
        speed = 2 - (weight/100)

        # Arrays
        stations = [] # LOAD: List of all Stations
        robots = []
        url = "http://127.0.0.1:5000/robots"
        

        # HELPING CODE
        # example for getting Robot from Database
        robot_id = 2
        url_get_robot = f"http://127.0.0.1:5000/robot/{robot_id}"
        response = requests.get(url_get_robot)
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
        else:
            obj_robot = json.loads(response.text)
            robot = Robot.from_dict(obj_robot)
            robot.charge()




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