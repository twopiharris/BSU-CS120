#!/usr/bin/python3.8

""" LinusOrGuido.py
    Illustrates if-elif-else structure
    Checks to see if the user
    has an appropriate open-source name
    """

firstName = input("Please enter your first name: ")

if firstName == "Guido":
    print("Thanks for writing Python")
elif firstName == "Linus":
    print("Linux Rocks!")
else:
    print("If you're going to be an open-source star,")
    print("you might need to get a cooler name.")
