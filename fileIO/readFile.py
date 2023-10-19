""" readFile.py
    read the contents of a text file
"""
def main():
    file = open("groceries.txt", "r")

    for line in file:
      line = line.strip()
      print ("we need {}, dude".format(line))

    file.close()

main()