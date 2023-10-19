""" writeFile.py
    demonstrates classic serial text output
"""

def main():
    file = open("groceries.txt", "w")
    file.write("eggs \n")
    file.write("milk \n")
    file.write("cereal \n")
    file.close()
    print ("Wrote grocery list")

    file = open("groceries.txt", "a")
    file.write("chocolate \n")
    file.close()
    print ("Updated grocery list")

main()
