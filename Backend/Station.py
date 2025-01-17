import heapq
class Station:
    def __init__(self, name, trias_id = None, lat = None, long = None) :
        self.name = name
        self.trias_id = trias_id
        self.lines = []
        self.lat = lat
        self.long = long
        self.connections = [] # Liste von Verbindungen (Zielstation, Gewicht, Linie)

    def to_dict_s(self):
        # Convert Package object to a dictionary
        return {
            "name": self.name,
            "trias_id": self.trias_id,
            "lines": self.lines,
            "lat": self.lat,
            "long": self.long,
            "connection": self.connections
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            trias_id = data['tris_id'],
            lines = data['lines'],
            lat=data['lat'],
            long = data['long'],
            connection = data['connection']
        )


    def add_connection(self, target_station, time, line) :
        self.connections.append([target_station, time, line])

    def add_line(self, line):
        self.lines.append(line)

    def get_lines(self):
        return self.lines
    
    def get_connection(self) :
         return self.connections
    
    def get_name(self):
        return self.name
    
    def get_triasID(self):
        return self.trias_id
    
    def get_lat(self):
        return self.lat
    
    def get_long(self):
        return self.long

def dijkstra(start_station, target_station):
    pq = []
    heapq.heappush(pq, (0, start_station))
    distance = {start_station: 0}
    previous = {start_station: None}

    while pq:
        timecost, current_station = heapq.heappop(pq)

        if current_station == target_station:
            path = []
            while current_station:
                path.append(current_station.name)
                current_station = previous[current_station]
            return timecost, path[::-1]

        for neighbour, time, line in current_station.get_connection():
            new_timecost = timecost + time
            if neighbour not in distance or new_timecost < distance[neighbour]:
                distance[neighbour] = new_timecost
                previous[neighbour] = current_station
                heapq.heappush(pq, (new_timecost, neighbour))
    return float('int'), []
