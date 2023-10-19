#!/usr/bin/python3.8

""" critterC.py
    using setter as a filter
"""


class Critter(object):

    def __init__(self):
        super().__init__()
        self.name = "Anonymous"
        self.age = 5

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

    def sayHi(self):
        print(f"Hi. My name is {self.name}")
        print(f"...and I am {self.age} years old")
        print()

def main():
    c = Critter()
    c.name = "Percival"
    c.age = -5
    c.age = "None of your business"
    c.sayHi()

if __name__ == "__main__":
    main()
