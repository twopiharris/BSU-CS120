""" inventory.py
    Demonstrates lists
    4/20/06 """

inventory = [
    "toothbrush",
    "suit of armor",
    "latte espresso",
    "crochet hook",
    "bone saw",
    "towel"]

print("I packed these things for my adventure:")
print(inventory)
print()

print("I love my {} and my {}".format(inventory[2], inventory[4]))
print()

print("my first few items:")
print(inventory[:3])
print()

print("Item # 3: {}".format(inventory[3]))
print()

print("changing third item...")

inventory[3] = "doily"

print("third item is now: {}".format(inventory[3]))
print()

print("revised inventory:")
print(inventory)
print()

print("adding kitchen sink")
inventory.append("kitchen sink")
print(inventory)
print()

print("never mind... I don't need that")
inventory.remove("kitchen sink")
print(inventory)
print()

for item in inventory:
    print ("I hit the dragon with my {}".format(item))

print("Hi there")

monsters = ("algebra beast", "it", "sasquatch")

