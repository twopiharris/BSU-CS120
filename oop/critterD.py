#!/usr/bin/python3.8

""" critterD.py
    Improving the initializer
"""

class Critter(object):

    def __init__(self, name = "anonymous", age = 5):
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

    def sayHi(self):
        print(f"Hi. My name is {self.name}")
        print(f"...and I am {self.age} years old")
        print()


def main():
    c1 = Critter()
    c1.sayHi()

    c2 = Critter("George", 27)
    c2.sayHi()

    c3 = Critter(name = "Martha")
    c3.sayHi()

if __name__ == "__main__":
    main()
