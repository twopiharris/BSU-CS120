""" pickleDemo.py
    demonstrates object serialization
    with pickle """

import pickle

class Critter(object):
  def __init__(self, name = "", age = 0):
    object.__init__(self)
    self.name = name
    self.age = age

def main():
  c = Critter("Lizzie Borden", 23)
  #Note here is a change in Python 3.*
  #file = open("serialKiller..dat", "w")
  #the file must now be written in binary mode
  file = open("serialKiller.dat", "wb")
  pickle.dump(c, file)
  file.close()

  file = open("serialKiller.dat", "rb")

  d = pickle.load(file)
  print (d.name)

  #save an entire list at once
  badCritters = [
    Critter("Darth Vader", 65),
    Critter("Knight who says 'Nii'", 43)
  ]

  file = open("badGuys.dat", "wb")
  pickle.dump(badCritters, file)
  file.close()

  #load them back in
  file = open("badGuys.dat", "rb")
  otherGuys = pickle.load(file)
  for guy in otherGuys:
    print (guy.name)

  file.close()

if __name__ == "__main__":
  main()
