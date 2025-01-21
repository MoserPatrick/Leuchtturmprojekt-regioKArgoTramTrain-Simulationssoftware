from package import Package
import random
import requests
from Station import Station

class package_creator:

    def create_package(numb_packages, package_list, pos):

        # TODO: get stations


        # get capacity and stations
        url = "http://127.0.0.1:5000/config"
        url_stations = "http://127.0.0.1:5000/stations"

        # Send a GET request to the server
        response = requests.get(url)
        response_stations = requests.get(url_stations)
        stations = response_stations.json()
        print(type(stations))
        stations_obj_list = []

        for station in stations:
            stations_obj = Station.from_dict(station)
            stations_obj_list.append(stations_obj)

       
        print("created station objects")

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

        for i in range(int(numb_packages)):
            # Random Package Generator
            # get weigth
            if (i != int(numb_packages)-1):
                weight = random.uniform(1.0, capacity/float(numb_packages))
                capacity -= weight
            else:
                if (int(numb_packages) > 1):
                    weight = random.uniform(1.0, capacity - weight)
                else:
                    weight = random.uniform(1.0, capacity)
            # get width
            width = random.uniform(1.0, 50.0)
            # get height
            height = random.uniform(1.0, 30.0)
            # get lenght
            length = random.uniform(1.0, 70.0)
            # get destination
            print("Getting Random Station")
            remaining_stations = [station for station in stations_obj_list if station != pos]
            dest = random.choice(remaining_stations)
            print("Random Station worked")

            # create Package
            package = Package(round(weight, 2), round(width, 2), round(height, 2), round(length, 2), dest)
            package_list.append(package)
            
        return package_list