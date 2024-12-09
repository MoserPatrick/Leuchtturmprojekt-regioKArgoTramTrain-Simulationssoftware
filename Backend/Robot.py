
class Robot:
#Constants
    carryCap = CARRYCAP
    homestation = HOMESTATION

#Constructor
    def __init__(self, id, pos, status, packageList):
        self.id = id 
        self.position = pos
        self.batteryStatus = status
        self.status = status
        self.packageList = packageList
        
        
#Methods
    def returnHome():
        pass
    def charge():
        pass
    def waitForNextTram():
        pass
    def findBestPath():
        pass
    def deliverPackage():
        pass
    def loadPackage():
        pass
