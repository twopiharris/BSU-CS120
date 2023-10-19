#!/usr/bin/python3.8

""" critterA.py
    A VERY simple object
"""

class Critter(object):

    def __init__(self):
        super().__init__()
        self.__name = "Anonymous"
        self.__age = 5

    def sayHi(self):
        print(f"Hi. My name is {self.__name}")
        print(f"...and I am {self.__age} years old")
        print()

def main():
    c = Critter()
    c.__name = "Floofie"
    c.sayHi()

if __name__ == "__main__":
    main()