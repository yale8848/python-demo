from util.Log import *

class Car():
    def __init__(self,name):
        self.name = name;
        pass

    def addEnergy(self):
        pass

    def run(self):
        p(self.name+ " : car run")
