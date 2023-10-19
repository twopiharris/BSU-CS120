def main():
    try:
    	userInput = input("please enter a number: ")
    	theNumber = int(userInput)
    	print(10/theNumber)

    except ValueError:
        print("That was not an integer")

    except:
        print("Something else went wrong")

if __name__ == "__main__":
    main()