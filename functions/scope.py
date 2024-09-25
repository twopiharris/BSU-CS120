#!/usr/bin/python3.8

""" scope.py
    illustrates scope and functions
    """

varOutside = "I was created outside the function"
print(f"outside the function, varOutside is: {varOutside}")

def theFunction():
    varInside = "I was made inside the function"

    print(f"inside the function, varOutside is: {varOutside}")
    print(f"inside the function, varInside is: {varInside}")

theFunction()

print(f"back outside the function, varOutside is: {varOutside}")
# if I uncomment the next line, the program will crash
print(f"back outside the function, varInside is: {varInside}")

