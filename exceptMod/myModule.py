#!/usr/bin/python3.8

""" My module
    Any python file can also be a module
    You can create functions for re-use
"""

def doAthing():
    print("I just did a thing")

def doAnotherThing():
    print("I just did the other thing")


# It's often good to have a main function for testing

def main():
    print("In the module, testing the functions:")
    doAthing()
    doAnotherThing()
    print(f"BTW my namespace is '{__name__}'")

#main()

#only run main if I am NOT imported
if __name__ == "__main__":
    main()
