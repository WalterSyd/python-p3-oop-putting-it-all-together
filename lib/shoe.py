#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size, condition="New"):
        self.brand = brand
        self.size = size
        self.condition = None

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,value):
        if not isinstance(value, int):
            print("size must be an integer", end="")
        else:
            self._size = value


    def cobble(self):
          print("your shoe is as good as new!\n", end="")
          return self

    def repair(self):
        self.condition = "New"


shoe1 = Shoe("Nike",10)
# print(shoe1.brand)
# print(shoe1.size)
print(shoe1.cobble())