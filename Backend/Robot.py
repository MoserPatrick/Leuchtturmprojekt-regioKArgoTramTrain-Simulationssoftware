from utils import Constants as CON
from create_package import package_creator
import time



class Robot:
#Constants
    carryCap = CON.CARRYCAP
    homestation = CON.HOMESTATION

#Constructor
    def __init__(self, id, pos, status, numb_packages, package_list, usage, capacity):
        self.id = id
        self.position = pos
        self.batteryStatus = status
        self.status = status
        self.numb_packages = numb_packages
        self.package_list = package_list
        self.usage = usage
        self.capacity = capacity
        
        
#Methods
    def returnHome():
        pass
    def charge():
        speed = 1 # simulation speed
        # Charging 1% at a time (for visuals)
        for status in range(100):
            time.sleep(1 * speed)
        # Charging everything at once but take the given time
        time.sleep((100 - status) * speed)
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
        del self.package_list(0)
        pass
    def loadPackage(self):
        self.package_list = package_creator.create_package(self.numb_packages, self.capacity, self.package_list)
        pass
