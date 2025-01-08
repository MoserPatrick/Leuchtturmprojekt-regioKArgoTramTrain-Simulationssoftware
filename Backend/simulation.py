from Robot import Robot
from package import Package
from create_package import package_creator
import requests


class Simulation:

    def main():

        # Create Robots
        # Configurated Data 
        numb_robots = 3 # LOAD: load the config data
        max_packages = 3 # LOAD: load the config number of Packages
        battery = 3
        capacity = 3
        sim_speed = 1.0
        usage = 1

        # Robot Data
        id = 1
        pos = "(100, 50)" # LOAD: load the real starting Position (Station)
        energy = 100 # LOAD: from config
        numb_packages =1
        package_list = 1
        status = "idle"
        dest = "None"
        speed = 1
        weight = 100.0 # LOAD: load form config

        # Arrays
        stations = [] # LOAD: List of all Stations
        robots = []
        url = "http://127.0.0.1:5000/robots"
        

        for i in range(numb_robots):
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

            robots.append(robot)

        #robot.charge()

        pass

    if __name__ == "__main__":
        main()