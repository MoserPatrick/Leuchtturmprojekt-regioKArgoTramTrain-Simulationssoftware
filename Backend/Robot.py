from utils import Constants as CON
from create_package import package_creator
import time



class Robot:
#Constants
    carryCap = CON.CARRYCAP
    homestation = CON.HOMESTATION

#Constructor
    def __init__(self, id, pos, energy, numb_packages, package_list, weight, status, dest, speed):
        self.id = id
        self.position = pos
        self.energy = energy
        self.numb_packages = numb_packages
        self.package_list = package_list
        self.weight = weight
        self.status = status
        self.dest = dest
        self.speed = speed
        

#Methods
    def returnHome():
        pass
    def charge(self):
        print("start")
        speed = 1 # simulation speed
        # Test Value battery = 95
        # Charging 1% at a time (for visuals)
        for battery in range(battery, 101):
            print(battery)
            time.sleep(1 * speed)
        # Charging everything at once but take the given time
        # time.sleep((100 - battery) * speed)
        pass
    def waitForNextTram():
        time = 12435 # simulation  time in seconds
        arrival_time = 12439 # arrival time of the Tram
        time.sleep(arrival_time - time)
        pass
    def findBestPath():
        pass
    def deliverPackage(self):
        time.sleep(1)
        del self.package_list[0]
        pass
    def loadPackage(self):
        self.package_list = package_creator.create_package(self.numb_packages, self.package_list)
        pass
