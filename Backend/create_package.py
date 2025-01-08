from package import Package
import random

class package_creator:

# TODO get capacity is missing
    def create_package(numb_packages, package_list):
        for i in range(numb_packages):
            '''# Random Package Generator
            # get weigth
            if (numb_packages[i+1]):
                weight = random.uniform(1.0, capacity)
                capacity -= weight
            else:
                weight = capacity
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
            package_list.append(package)
            '''
            # Dummy Data package Generator
            package_list.append(Package(30, 30, 10, 50, (100,100)))
        return package_list