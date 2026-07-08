# from abc import *
# abc = absarct base class
from abc import ABC, abstractmethod

class Shape(ABC) :
    @abstractmethod
    def area(self):
        pass