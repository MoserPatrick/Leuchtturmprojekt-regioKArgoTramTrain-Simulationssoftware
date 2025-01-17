from Station import Station
class Package:
    
#Constructor
    def __init__(self, weight, width, height, length, destination):
        self.weight = weight 
        self.width = width
        self.height = height
        self.length = length
        self.destination = destination
    
    def to_dict_p(self):
        # Convert Package object to a dictionary
        return {
            "weight": self.weight,
            "width": self.width,
            "height": self.height,
            "length": self.length,
            "destination": self.destination if isinstance(self.destination, dict) else self.destination.to_dict_s()
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            weight=data['weight'],
            width = data['width'],
            height = data['height'],
            length = data['length'],
            destination = Station.from_dict(data['destination'])
            )