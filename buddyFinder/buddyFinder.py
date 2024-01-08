#!/usr/bin/python3.8

import random, datetime

""" buddyFinder.py
    asks for section
    creates a randomized list of student pairs
    seeds on date so everyone gets same list on same day
    consider making web-based

    Andy Harris, CS120, Aug 2023
"""

def main():

    keepGoing = True
    while(keepGoing):
        result = menu()
        if result == "0":
            keepGoing = False
        elif result == "1":
            fileName = "CS120_2_s24.txt"
        elif result == "2":
            fileName = "CS120_3_s24.txt"

        if keepGoing:
            studentList = makeList(fileName)
            pairList = makePairs(studentList)

            print("Pairs: ")
            for pair in pairList:
                (student1, student2) = pair
                print(f"{student1:25} {student2:25}")

def seed():
    """ use datetime module to seed the random generator
        gives the same results on the same day
    """

    today = datetime.datetime.now()
    dateString = ""
    dateString += str(today.month)
    dateString += str(today.day)
    dateString += str(today.year)
    #print (dateString)
    dateInt = int(dateString)
    #print (dateInt)
    random.seed(dateInt)

def menu():
    """ presents CLI menu to manage
        input user input
    """

    keepGoing = True
    while (keepGoing):
        print("""

        0) quit
        1) 9:00 session
        2) 10:00 session
        """)

        result = input("Your choice: ")
        if result in ("0", "1", "2"):
            keepGoing = False
        else:
            print("Please enter 0, 1, or 2")

    return result

def makeList(fileName):
    """ given the filename of a data file
        produces a list containing student
        names
    """

    studentList = []

    inFile = open(fileName, "r")
    for line in inFile:
        line = line.replace('"', '')
        studentList.append(line.strip())

    print(f"Number of students: {len(studentList)}")
    inFile.close()
    return(studentList)


def makePairs(studentList):
    """ given a list of student names,
        creates a randomized list of pairs
        If there is an odd number of students,
        one is paired with "Null"
    """

    seed()
    pairList = []
    keepGoing = True

    while keepGoing:

        if len(studentList) == 1:
            student1 = studentList[0]
            student2 = "NULL"
            keepGoing = False
        elif len(studentList) <= 0:
            keepGoing = False
        else:
            student1 = random.sample(studentList, 1)[0]
            #print(f"s1: {student1}")
            studentList.remove(student1)

            student2 = random.sample(studentList, 1)[0]
            #print(f"s2: {student2}")
            studentList.remove(student2)

        pairList.append((student1, student2))

    return pairList

if __name__ == "__main__":
    main()
