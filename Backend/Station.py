import heapq
from jsonreader import generate_stationlist
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
            "long": self.long
        }
    
    @classmethod
    def from_dict(cls, data):
        # Create instance with required parameters only
        station = cls(
            name=data.get('name'),
            trias_id=data.get('trias_id'),
            lat=data.get('lat'),
            long=data.get('long')
        )

        # Assign lists separately to avoid passing unknown arguments
        station.lines = data.get('lines', [])  # Default to an empty list if missing

        #station.connections = data.get('connections', [])  # Default to an empty list

    @classmethod
    def from_dict_s(cls, data):
        # Create instance with required parameters only
        station = cls(
            name=data.get('name'),
            trias_id=data.get('trias_id'),
            lat=data.get('lat'),
            long=data.get('long')
        )

        # Assign lists separately to avoid passing unknown arguments
        station.lines = data.get('lines', [])  # Default to an empty list if missing
        
        #station.connections = data.get('connections', [])  # Default to an empty list

        return station


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

