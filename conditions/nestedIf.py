#!/usr/bin/python3.8

temp = input("Temperature: ")
temp = int(temp)

if temp < 70:
    if temp < 32:
        print("cold")
    else:
        print ("cool")
else:
    if temp > 80:
        print("hot")
    else:
        print ("warm")




if temp > 80:
    print("hot")
elif temp > 70:
    print("warm")
elif temp > 32:
    print ("cool")
else:
    print("cold")

