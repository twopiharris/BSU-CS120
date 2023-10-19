#!/usr/bin/python3.8
import math

""" critter.py
    basic object demonstration """

class Critter(object):

    def __init__(self, name = "Anonymous", age = 5):
        super().__init__()
        self.name = name
        self.age = age
        self.angle = 0

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
        if value < 0:
            print("age can't be negative")
            value = 0

        self.__age = value

    @property
    def angle(self):
        return (self.__angle * 180) / math.pi

    @angle.setter
    def angle(self, value):
        self.__angle = (value * math.pi) / 180

    def sayHi(self):
        print(f"Hi, my name is {self.name} and I'm {self.age} years old")

def main():
    c = Critter("Martha")

    c.sayHi()
    c.name ="George"
    c.age = -3
    print(f"I am also called {c.name}")
    print(f"I'm {c.age} years old.")

if __name__ == "__main__":
    main()
