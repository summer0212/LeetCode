class ParkingSystem:

    def __init__(self, big, medium, small):
        self.big  = big 
        self.medium = medium
        self.small = small
        
        

    def addCar(self, carType) :
        if carType == 1:
            if self.big > 0:
                self.big = self.big - 1
                print(self.big)

                return True
            else:
                return False
        elif carType == 2:
            if self.medium > 0:
                self.medium = self.medium -1
                print(self.medium)
                return True
            else:
                return False
        elif carType == 3:
            if self.small > 0:
                self.small = self.small - 1
                print(self.small)
                return True
            else:
                return False
            
            





# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(2, 0, 2)
param_1 = obj.addCar(1)
param_2 = obj.addCar(1)
param_3 = obj.addCar(1)
print(param_1)
print(param_2)
print(param_3)
