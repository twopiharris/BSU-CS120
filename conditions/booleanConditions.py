#!/usr/bin/python3.8

fName = input("First name: ")
lName = input("LastName: ")

# this does work as expected
if fName == "Alan" and lName == "Turing":
    print("Thanks for the main ideas of computer science.")

# this also works...
if lName == "Kay" or lName == "Turing":
    print("You must be Alan")


# This makes sense in English
# it DOES NOT do what you think!

if lName == "Kay" or "Turing":
    print("Hi Alan!")


# negatives are very messy - See DeMorgan's law
# this will NOT work like you probably think
if lName != "Kay" or lName != "Turing":
    print ("You must not be Alan")

# is (not A) and (not B) the same as not (A and B)?
# is (not A) or (not B) the same as not (A or B)?


#more complex conditions are also messy...

# this works...
if (fName == "Alan" and (lName == "Turing" or lName == "Kay")):
    print ("You are a famous computer scientist")

# but it's confusing, and order of operations can be a problem
# is (A or B) and C
# the same as
# A or (B and C)?
# and what does A or B and C mean?


# better solution for beginners:

# Use nested ifs for 'and'
if fName == "Alan":
    if lName == "Kay":
        print ("Thanks for object-oriented programming!")

# bonus: you can have more specific else clauses
if fName == "Alan":
    if lName == "Kay":
        print ("Thanks for object-oriented programming!")
    else:
        print ("I was looking for Alan Kay")
else:
    print ("I was looking for someone named 'Alan'")


# use parallel ifs for 'or'
# bonus, messages can be different, so can else clauses
if lName == "Turing":
    print ("Thanks for CS")
if lName == "Kay":
    print ("Thanks for OOP")

#you can create very complex logic with good nesting
if fName == "Alan":
    print ("Alan is a famous name in CS")
    if lName == "Turing":
        print ("Turing machines are amazing")
    elif lName == "Kay":
        print ("OOP is amazing")
else:
    print ("I'm only interested in people named 'Alan'")
"""
"""




