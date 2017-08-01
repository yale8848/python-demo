from util.Log import *
from electric.Car import Car

class ElectricCar(Car):
    def __init__(self,name):
        super().__init__(name)

    def addEnergy(self):
        p(self.name+" : add electric")