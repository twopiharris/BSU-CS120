""" password attempt """

correct = "Python"
guess = ""
tries = 0


while ((guess != correct) and (tries < 3)):
    guess = input("Password: ")
    if guess == correct:
        print("you win")
    else:
        tries += 1
        if tries >= 3:
            print("Too many guesses")

"""
while (True):
    guess = input("Password: ")
    tries += 1

    if guess == correct:
        print ("Good job!")
        break

    if tries >= 3:
        print("Too many tries")
        break
"""

"""
while tries < 3:
    guess = input("Password: ")
    tries += 1
    if guess == correct:
        tries = 3

"""

"""
keepGoing = True
while(keepGoing):
    tries += 1
    guess = input("password: ")
    if guess == correct:
        print("Good job")
        keepGoing = False
    if tries >= 3:
        print("You lose")
        keepGoing = False

"""