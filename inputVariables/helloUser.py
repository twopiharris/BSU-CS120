#!/user/bin/python3.8

""" helloUser.py
    takes user input and generates
    a customized greeting
"""

#ask user name, store in userName as string
userName = input("What is your name? ")

#greet user by name
print (f"Hi there, {userName}!")

#ask for favorite color, put in color as string
color = input(f"What is you're favorite color, {userName}? ")

#put multiple variables in f-string
print(f"{color} is a nice color, {userName}.")

#the older .format technique is still sometimes used
print("I love the color {}, {}.".format(color, userName))
