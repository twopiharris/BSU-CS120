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
    def hitPoints(value)
        self.__hitPoints = value

    @property
    def hitChance(self):
        return self.__hitChance

    @hitChance.setter
    #must be integer between 0 and 100
    def hitChance(self, value):
        self.__hitChance = value

    @property
    def maxDamage(self):
        return self.__maxDamage

    @maxDamage.setter
    #we'll allow maxDamage to be negative. That's a healer!
    def maxDamage(self, value):
        self.__maxDamage = value

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    #armor must be a number, but it can be negative (cursed)
    def armor(self, value):
        self.__armor = value

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

            #calculate the damage
            #consider enemy armor
            #if damage is negative, ignore it
            #subtract damage from enemy's hp
