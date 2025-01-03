from Robot import Robot
from package import Package
from create_package import package_creator


class Simulation:

    def main():

        # Create Robots
        # Configurated Data 
        stations = [] # LOAD: List of all Stations
        numb_robots = 3 # LOAD: load the config data
        robots = []
        numb_packages = 3 # LOAD: load the config number of Packages
        pos = (100, 50) # LOAD: load the real starting Position (Station)
        status = 100 # LOAD: from config
        usage = 500 # LOAD: load from config
        capacity = 30 # LOAD: load form config


        for robots in numb_robots:
            # Create package_list
            package_list = []    
            # creating packages 
            package_list = package_creator.create_package(numb_packages, capacity, package_list)
            
            robot = Robot(robots, pos, status,  package_list, usage, capacity)
            robots.append(robot)


        pass

    if __name__ == "__main__":
        main()