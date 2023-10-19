#!/usr/bin/python3.8
""" loadCSV.py
    use csv module to load a CSV data file
"""

import csv

def main():
    fileIn = open("contacts.csv", "r")
    data = csv.reader(fileIn)
    for row in data:
        (name, company, email) = row
        print(f"{name:20}{company:15}{email:15}")

main()