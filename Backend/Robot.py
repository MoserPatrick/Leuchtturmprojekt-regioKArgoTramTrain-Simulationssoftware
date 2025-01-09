from utils import Constants as CON
from create_package import package_creator
import time
from package import Package
import sqlite3
import json
import requests


class Robot:
#Constants
    carryCap = CON.CARRYCAP
    homestation = CON.HOMESTATION

#Constructor
    def __init__(self, id, position, energy, numb_packages, package_list, status, dest, speed, weight):
        self.id = id
        self.position = position
        self.energy = energy
        self.numb_packages = numb_packages
        self.package_list = package_list
        self.status = status
        self.dest = dest
        self.speed = speed
        self.weight = weight
    
    @classmethod
    def from_dict(cls, data):
        # Recreate Robot from a dictionary
        packages = [Package.from_dict(pkg) for pkg in data['package_list']]
        return cls(
            id=data['id'],
            position=data['position'],
            energy=data['energy'],
            numb_packages=data['numb_packages'],
            package_list = packages,
            status = data['status'],
            dest = data['dest'],
            speed = data['speed'],
            weight = data['weight']
        )
        
     
#Methods
    def to_dict(self):
        # Convert object state to a dictionary (excluding methods)
        return {
            "id": self.id,
            "position": self.position,
            "energy": self.energy,
            "numb_packages": self.numb_packages,
            "package_list": [package.to_dict_p() for package in self.package_list],  # Serialize the list of objects,
            "status": self.status,
            "dest": self.dest,
            "speed": self.speed,
            "weight": self.weight
        }
    
    
    # Serialize package_list to a JSON string
    def insert_robot(robot):
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()

        # Serialize package_list to a JSON string
        package_list_json = json.dumps([package.to_dict_p() for package in robot.package_list])

        # Insert robot into the database (assuming you have a `robots` table)
        cursor.execute('''
            INSERT INTO robots (id, name, package_list) 
            VALUES (?, ?, ?)
        ''', (robot.id, robot.name, package_list_json))

    def returnHome():
        #TODO add homepath
        pass
    def charge(self):
        print("Charging for ", self.energy)
        url_get_config = "http://127.0.0.1:5000/config"
        response = requests.get(url_get_config)
        json_response = json.loads(response.text)
        capacity = json_response['capacity']
        sim_speed = json_response['sim_speed']

        # Charging 1% at a time (for visuals)
        '''for energy in range(energy, 101):
            print(energy)
            time.sleep(1 * speed)'''
        # Charging everything at once but take the given time
        if(self.energy > capacity):
            self.energy = capacity
        time.sleep((capacity - self.energy) * sim_speed)
        #self.energy = capacity
        self.energy = 1000.0
        url_patch_robot = f"http://127.0.0.1:5000/robot/{self.id}"
        json_robot = self.to_dict()
        print("enery", json_robot['energy'])
        response = requests.patch(url_patch_robot, json=json_robot)

        pass
    def waitForNextTram():
        time = 12435 # simulation  time in seconds
        arrival_time = 12439 # arrival time of the Tram
        time.sleep(arrival_time - time)
        pass
    def findBestPath():
        # TODO add pathfinding
        pass
    def deliverPackage(self):
        time.sleep(1)
        del self.package_list[0]
        pass
    def loadPackage(self):
        self.package_list = package_creator.create_package(self.numb_packages, self.package_list)
        pass
