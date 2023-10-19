#!/usr/local/bin/python3.8

""" nameGame.py
    illustrate basic string functions
    Andy Harris
    3/15/06"""

userName = input("Please tell me your name: ")
#print ("Hi there, {}!".format(userName))
print (f"Hi there, {userName}")

print ("I will shout your name: {}".format(userName.upper()))
print ("Now all in lowercase: {}".format(userName.lower()))
print ("How about inverting the case? {}".format(userName.swapcase()))
numChars = len(userName)
print ("Your name has {} characters".format(numChars))
print ("Now I'll pronounce your name like a cartoon character:")

userName = userName.upper()
#print(userName)
userName = userName.replace("R", "W")
#print(userName)
userName = userName.title()
print (userName)
