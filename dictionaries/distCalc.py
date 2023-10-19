#!/usr/bin/python3.8

""" distCalc.py
    calculate distance with a 2d list"""

#tuples for data
cityName = ("Indianapolis",
            "New York",
            "Tokyo",
            "London")

distance = (
  (0, 648, 6476, 4000),
  (648, 0, 6760, 3470),
  (6476, 6760, 0, 5956),
  (4000, 3470, 5956, 0)
)

def getCity(title):
  """ gets a city number """
  keepGoing = True
  while (keepGoing):
    print (f"""
    {title}
    0) Indianapolis
    1) New York
    2) Tokyo
    3) London
    """)
    cityNum = input("City: ")
    if cityNum in ("0", "1", "2", "3"):
      keepGoing = False
    else:
      print("That is not a correct input. Please try again")

  cityNum = int(cityNum)
  return cityNum

def main():
    """ gets two cities, determines distance between them """

    fromID = getCity("Traveling from...")
    toID = getCity("Traveling to...")

    result = distance[fromID][toID]
    cityFrom = cityName[fromID]
    cityTo = cityName[toID]

    print (f"Distance from {cityFrom} to {cityTo} is {result} miles")

main()
