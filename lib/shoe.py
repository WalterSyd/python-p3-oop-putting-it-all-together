#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer\n", end="")
        else:
            self._size = value


    def cobble(self):
          print("Your shoe is as good as new!\n", end="")
         

    def makes_new(self):
        self.condition = "New"


shoe1 = Shoe("Nike",10)
# print(shoe1.brand)
# print(shoe1.size)
print(shoe1.condition)
print(shoe1.cobble())
