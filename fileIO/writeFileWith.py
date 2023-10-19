""" write and read a file using the with operator
"""
def main():
    with open("MyFile.txt", "w") as outFile:
        outFile.write("eggs \n")
        outFile.write("milk \n")
        outFile.write("cookies \n")

        #close is not necessary

    with open("MyFile.txt", "r") as inFile:
        for line in inFile:
            print(line.strip())

        #close is not necessary

main()