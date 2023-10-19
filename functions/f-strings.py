#!/usr/bin/python3.8

""" f-strings and formatting """

def main():
    """ demonstrate various options for f-strings """

    className = "CS 120"
    numStudents = 33
    pi = 3.1415927
    avg = .85

    # ordinary print
    print(f"{className} has {numStudents} students and pi is {pi}")

    # add column widths
    print(f"|{className:15}|{numStudents:5}|{pi:10}|")

    # alignment
    print(f"|{className:^15}|{numStudents:<5}|{pi:>10}|")

    #formatting a float
    print(f"{pi} {pi:.4f} {pi:.2f}")

    #doing a percentage
    print(f"{avg:%} {avg:.2%} {avg:.0%}")

    # base conversion
    print(f"binary: {numStudents:8b}, octal: {numStudents:3o} hex: {numStudents:2x}")


main()
