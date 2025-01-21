
import requests
import json
import sqlite3
from Station import Station
from jsonreader import jsonreader as jread
class Prepare:
    @classmethod
    async def start():
        connection = sqlite3.connect('Backend/simulation.db')
        cursor = connection.cursor()

        stationlist = []
        numbers = ['1', '2', '3', '4', '5', '8', '17', '18', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S11', 'S12', 'S31', 'S32', 'S33', 'S51', 'S52', 'S71', 'S81']
        # Lade alle Daten aus der stations-Tabelle
        for table_name in numbers:
            query = f'SELECT name, trias_id, lines, lat, long FROM "line_{table_name}"'
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                name, trias_id, lines_json, lat, long = row
                lines = json.loads(lines_json)  # Konvertiere das JSON-String zurück in ein Array
                station = Station(name, trias_id, lat, long)
                for line in lines:
                    station.add_line(line)
                stationlist.append(station)
        connection.close()
        trias_id_list, numbers = jread.get_lines_and_stations()
        jread.add_lines_to_stations(stationlist, trias_id_list, numbers)
        sorted_stationlist = jread.sort_stationlist(stationlist, trias_id_list)
        jread.calculate_weight_and_create_connections(sorted_stationlist, numbers)
        inverted_sorted_stationlist = []
        for i in range (len(sorted_stationlist)):
                inverted_sorted_stationlist.append(sorted_stationlist[i][::-1])
        jread.calculate_weight_and_create_connections(inverted_sorted_stationlist, numbers)
        
        url_get_robots = f"http://127.0.0.1:5000/robots"
        response = await requests.get(url_get_robots)
        robotlist = json.loads(response)
        robotsdijkstra = []
        for robot in robotlist:
            dest, start = robot.getdestandstart()
            dest_id = dest.get_name()
            start_id = start.get_name()
            shortest_path, shortest_distance = jread.dijkstra(start_id, dest_id, stationlist)
            print("short", shortest_path)
            print("shortest", shortest_distance)
            robotsdijkstra.append(shortest_path)
        return robotsdijkstra