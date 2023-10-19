#!/usr/bin/python3.8

""" exceptDemo.py """
import sys

def main():
    """ test exception handling """

    keepGoing = True
    while keepGoing:
        #begin with the assumption everything went well
        keepGoing = False
        try:
            number = input("please enter an integer: ")
            number = int(number)
            print(f"10 / {number} = {10 / number}")

        except ValueError:
            print("that's not an integer")
            keepGoing = True

        except ZeroDivisionError:
            print("can't divide by zero")
            keepGoing = True

        except:
            print("Something went wrong")
            print(sys.exc_info())
            keepGoing = True

if __name__ == "__main__":
    main()