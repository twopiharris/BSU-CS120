#!/usr/bin/python3.8

import critterD

""" glitterCritter.py
    illustrates inheritance, method overriding
"""

class GlitterCritter(critterD.Critter):
    def __init__(self, name = "Gloria", age = 3):
        super().__init__(name, age)

    #overridden sayHi() method

    def sayHi(self):
        print(f"{self.name} gently shimmers.")

    #new spin method
    def spin(self):
        print(f"{self.name} spins around!")

def main():
    gc = GlitterCritter("Floofie")
    gc.sayHi()
    gc.spin()

if __name__ == "__main__":
    main()