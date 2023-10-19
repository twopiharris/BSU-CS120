#!/usr/bin/python3.8

""" critterB.py
    making the name into a property
"""


class Critter(object):

    def __init__(self):
        super().__init__()
        self.name = "Anonymous"
        self.__age = 5

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def sayHi(self):
        print(f"Hi. My name is {self.name}")
        print(f"...and I am {self.__age} years old")
        print()

def main():
    c = Critter()
    c.sayHi()
    c.name = "Percival"
    c.sayHi()

if __name__ == "__main__":
    main()
