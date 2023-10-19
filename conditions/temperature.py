#!/usr/bin/python3.8

temp = input("What's the temp? ")

temp = int(temp)

if temp < 32:
    print("Wear mittens")
elif temp < 50:
    print ("Wear a sweater")
elif temp < 70:
    print ("wear a t-shirt")
else:
    print("It's pretty hot out ...")


