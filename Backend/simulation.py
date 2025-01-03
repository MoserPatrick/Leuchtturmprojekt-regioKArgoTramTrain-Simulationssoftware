from Robot import Robot
from package import Package

class Simulation:

    def main():

        # Create Robots
        # Configurated Data 
        numb_robots = 3 # LOAD: load the config data
        numb_package = 3 # LOAD: load the config number of Packages
        pos = (100, 50) # LOAD: load the real starting Position (Station)
        status = 100 # LOAD: 
        for robots in numb_robots:
            # Create packageList
            packageList = []    
            for i in range(numb_package):
                package = Package(20, 30, 10, 50, ))

                packageList.append(package)
            
            robot = Robot(robots, pos, status, packageList, usage, capacity)


        '''def __init__(self, id, pos, status, packageList, usage, capacity):
        self.id = id
        self.position = pos
        self.batteryStatus = status
        self.status = status
        self.packageList = packageList
        self.usage = usage
        self.capacity = capacity'''

        pass

    if __name__ == "__main__":
        main()