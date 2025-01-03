from Robot import Robot
from package import Package
import random

class Simulation:

    def main():

        # Create Robots
        # Configurated Data 
        stations = [] # LOAD: List of all Stations
        numb_robots = 3 # LOAD: load the config data
        robots = []
        numb_package = 3 # LOAD: load the config number of Packages
        pos = (100, 50) # LOAD: load the real starting Position (Station)
        status = 100 # LOAD: 
        usage = 500 # LOAD:
        capacity = 30 # LOAD:


        for robots in numb_robots:
            # Create packageList
            packageList = []    
            for i in range(numb_package):
                '''# Random Package Generator
                # get weigth
                weight = random.uniform(1.0, 100,0)
                # get width
                width = random.uniform(1.0, 50,0
                # get height
                height = random.uniform(1.0, 30,0)
                # get lenght
                length = random.uniform(1.0, 70,0))
                # get destination
                dest = random.choice(stations)

                # create Package
                package = Package(weigth, width, height, length, dest)
                packageList.append(package)
                '''
                # Filler Data package Generator
                package = Package(20, 30, 10, 50, (100,100))
                packageList.append(package)
            
            robot = Robot(robots, pos, status, packageList, usage, capacity)
            robots.append(robot)


        pass

    if __name__ == "__main__":
        main()