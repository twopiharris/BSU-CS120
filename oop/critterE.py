#!/usr/bin/python3.8

""" critterE.py
    filtering property i/o
    and making virtual properties
    note we want user to enter angle
    in degrees, but we'll store as
    radians
"""
import math

class Critter(object):

    def __init__(self, name = "anonmymous", age = 5):
        super().__init__()
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if type(value) == int:
            if value >= 0:
                self.__age = value
            else:
               print("age must be positive")
               self.__age = 1
        else:
            print("age must be a number")
            self.__age = 1

    @property
    def ageInTen(self):
        return self.age + 10

    @property
    def angle(self):
        return (self.__angle * 180) / math.pi

    @angle.setter
    def angle(self, value):
        self.__angle = (value * math.pi) / 180


    def sayHi(self):
        print(f"Hi. My name is {self.name}")
        print(f"...and I am {self.age} years old")
        print()


def main():
    c = Critter()
    c.angle = 180
    print(c.ageInTen)

if __name__ == "__main__":
    main()
