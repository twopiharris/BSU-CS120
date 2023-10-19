#!/usr/bin/python3.8
import random

""" tbc.py
    module for basic turn-based combat
    includes a character class and a
    runFight function """


class Character(object):
    def __init__(self, name = "Goofbert",
               hitPoints = 10,
               hitChance = 50,
               maxDamage = 5,
               armor = 0):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor

    #define basic properties

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def hitPoints(self):
        return self.__hitPoints

    @hitPoints.setter
    #must be an integer, but it can go negative
    def hitPoints(self, value):
        if type(value) == int:
            newValue = value
        else:
            newValue = 1
        self.__hitPoints = newValue

    @property
    def hitChance(self):
        return self.__hitChance

    @hitChance.setter
    #must be integer between 0 and 100
    def hitChance(self, value):
        if type(value) == int:
            if value >= 0:
                if value <= 100:
                    newValue = value
                else:
                    newValue  = 100
            else:
                newValue = 0
        else:
            newValue = 0
        self.__hitChance = newValue

    @property
    def maxDamage(self):
        return self.__maxDamage

    @maxDamage.setter
    #we'll allow maxDamage to be negative. That's a healer!
    def maxDamage(self, value):
        if type(value) == int:
            newValue = value
        self.__maxDamage = newValue

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    #armor must be a number, but it can be negative (cursed)
    def armor(self, value):
        if type(value) == int:
            newValue = value
        else:
            newValue = 0

        self.__armor = newValue

    def printStats(self):
        print(f"""
    {self.name}
    ==================
    Hit points: {self.hitPoints}
    Hit chance: {self.hitChance}
    Max damage: {self.maxDamage}
    Armor:      {self.armor} """)

        print()

    def hit(self, enemy):
        """ calculates whether we hit enemy
            and how much damage we cause """
        #did we hit enemy?
        if random.randint(1, 100) < self.hitChance:
            print(f"{self.name} hits {enemy.name}...")

            #calculate the damage
            damage = random.randint(1, self.maxDamage)
            print(f"  for {damage} points of damage")
            #consider enemy armor
            print(f"  {enemy.name}'s armor can absorb {enemy.armor} points")
            damage -= enemy.armor
            #if damage is negative, ignore it
            if damage < 0:
                damage = 0
            #subtract damage from enemy's hp
            enemy.hitPoints -= damage

class UserCharacter(Character):
    def __init__(self, name = "",
                 hitPoints = 10,
                 hitChance = 50,
                 maxDamage = 5,
                 armor = 0):
        super().__init__(name, hitPoints, hitChance, maxDamage, armor)

    def chooseAction(self, enemy):
        """ allow user some choices """
        print(f"""{self.name}'s turn:
        1) heal
        2) rest
        3) attack """)
        userChoice = input("Which will you do? ")
        if userChoice == "1":
            healAmount = random.randint(1, 3)
            print (f"You healed {healAmount} points")
            self.hitPoints += healAmount
        elif userChoice == "2":
            damageIncrease = random.randint(1, 5)
            print("You've gotten a little stronger")
            self.maxDamage += damageIncrease
        else:
            #use the standard hit method to attack
            self.hit(enemy)

def playerFight(player1, player2):
    # keep fighting until somebody wins
    keepGoing = True
    userPlaying = False
    while keepGoing:
        if isinstance(player1, UserCharacter):
            userPlaying = True
            player1.chooseAction(player2)
        else:
            player1.hit(player2)

        if isinstance(player2, UserCharacter):
            userPlaying = True
            player2.chooseAction(player1)
        else:
            player2.hit(player1)

        print (f"{player1.name}: {player1.hitPoints} HP")
        print (f"{player2.name}: {player2.hitPoints} HP")
        print()

        if player2.hitPoints <= 0:
            print(f"{player1.name} wins!")
            keepGoing = False
        elif player1.hitPoints <= 0:
            print(f"{player2.name} wins!")
            keepGoing = False
        if userPlaying == False:
            dummy = input("press <ENTER> for another round: ")

def fight(player1, player2):
    keepGoing = True
    while keepGoing:
        player1.hit(player2)
        player2.hit(player1)

        print(f"{player1.name}: {player1.hitPoints}")
        print(f"{player2.name}: {player2.hitPoints}")

        if player2.hitPoints <= 0:
            print(f"{player1.name} wins!")
            keepGoing = False
        elif player1.hitPoints <= 0:
            print(f"{player2.name} wins!")
            keepGoing = False

        dummy = input("Press ENTER for another round...")

def main():
    c = Character()
    print("testing default character")
    c.printStats()

    print("testing auto fight")
    good = Character("Good")
    evil = Character("Evil")

    fight(good, evil)

    print("testing player fight")
    me = UserCharacter("Knowledge")
    enemy = Character("Ignorance")

    playerFight(me, enemy)

if __name__ == "__main__":
    main()
