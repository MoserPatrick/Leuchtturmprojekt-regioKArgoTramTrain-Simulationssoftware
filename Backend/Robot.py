from utils import Constants as CON
from create_package import package_creator
import time
from package import Package
import sqlite3
import json
import requests
import random


class Robot:
#Constants
    carryCap = CON.CARRYCAP
    homestation = CON.HOMESTATION

#Constructor
    def __init__(self, id, position, energy, numb_packages, package_list, status, dest, speed, weight, start_pos):
        self.id = id
        self.position = position
        self.energy = energy
        self.numb_packages = numb_packages
        self.package_list = package_list
        self.status = status
        self.dest = dest
        self.speed = speed
        self.weight = weight
        self.start_pos = start_pos
    
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
            weight = data['weight'],
            start_pos = data['start_pos']
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
            "weight": self.weight,
            "start_pos": self.start_pos
        }
    
    
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

        # Charging everything at once but take the given time
        if(self.energy > capacity):
            self.energy = capacity
        time.sleep((capacity - self.energy) * sim_speed)
        #self.energy = capacity
        self.energy = 1000.0
        url_patch_robot = f"http://127.0.0.1:5000/robot/{self.id}"
        json_robot = self.to_dict()
        requests.patch(url_patch_robot, json=json_robot)
        pass


    def waitForNextTram(self):
        # TODO
        time = 12435 # simulation  time in seconds
        arrival_time = 12439 # arrival time of the Tram
        self.status = "Waiting"
        url_patch_robot = f"http://127.0.0.1:5000/robot/{self.id}"

        json_robot = self.to_dict()
        requests.patch(url_patch_robot, json=json_robot)

        time.sleep(arrival_time - time)

        self.status = "Driving"
        json_robot = self.to_dict()
        requests.patch(url_patch_robot, json=json_robot)
        pass


    def findBestPath():
        # TODO add pathfinding
        pass


    def delieverPackage(self):
        deliver_time = 10
        url_patch_robot = f"http://127.0.0.1:5000/robot/{self.id}"
        self.status = "Delivering"

        json_robot = self.to_dict()
        requests.patch(url_patch_robot, json=json_robot)

        time.sleep(deliver_time)
        del self.package_list[0]
        if (self.package_list[0]):
            self.findBestPath
            self.status = "Delivering"
        else:
            self.returnHome
            self.status = "Returning Home"
        # 10% chance fopr the Package not being picked up.
        chance = random.uniform(0.0,100.0)
        if( chance > 90.0):
            print("Package was not picked up!")
        
        json_robot = self.to_dict()
        requests.patch(url_patch_robot, json=json_robot)
        pass


    def loadPackage(self):
        loading_time = 10
        url_patch_robot = f"http://127.0.0.1:5000/robot/{self.id}"
        self.status = "Loading"

        json_robot = self.to_dict()
        requests.patch(url_patch_robot, json=json_robot)

        time.sleep(loading_time)
        self.package_list = package_creator.create_package(self.numb_packages, self.package_list)
        self.findBestPath()
        self.status = "Driving"

        json_robot = self.to_dict()
        requests.patch(url_patch_robot, json=json_robot)
        pass
