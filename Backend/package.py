class Package:
    
#Constructor
    def __init__(self, weight, width, height, length, destination):
        self.weight = weight 
        self.width = width
        self.height = height
        self.length = length
        self.destination = destination
    
    def to_dict(self):
        # Convert Task object to a dictionary
        return {
            "weight": self.weight,
            "width": self.width,
            "height": self.height,
            "length": self.length,
            "destination": self.destination
        }
        