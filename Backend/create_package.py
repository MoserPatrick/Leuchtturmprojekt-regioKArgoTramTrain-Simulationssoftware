from package import Package
import random
import requests

class package_creator:

    def create_package(numb_packages, package_list):

        # TODO: get stations


        # get capacity 
        url = "http://127.0.0.1:5000/config"

        # Send a GET request to the server
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse and print the JSON response
            data = response.json()
            print("Retrieved Data:", data)
            capacity = data.get("capacity")
            print("capacity: ", capacity)
        else:
            print(f"Error: Received status code {response.status_code}")
            print("Message:", response.text)

        for i in range(numb_packages):
            '''# Random Package Generator
            # get weigth
            if (numb_packages[i+1]):
                weight = random.uniform(1.0, capacity)
                capacity -= weight
            else:
                weight = capacity
            # get width
            width = random.uniform(1.0, 50,0)
            # get height
            height = random.uniform(1.0, 30,0)
            # get lenght
            length = random.uniform(1.0, 70,0)
            # get destination
            dest = random.choice(stations)

            # create Package
            package = Package(weight, width, height, length, dest)
            package_list.append(package)'''
            
            # Dummy Data package Generator
            package = Package(30, 30, 10, 50, (100,100))
            package_list.append(package)
        return package_list