""" csvDemo.py
    reading content from comma-seperated values (CSV) files
    expects contacts.csv to have name, company, email
    one record per line
"""

file = open("contacts.csv", "r")
for line in file:
  #print(line)
  line = line.strip()
  line = line.replace('"', '')
  currentLine = line.split(",")
  #print(currentLine)
  (name, company, email) = currentLine


  print ("{:15}{}".format("Name:",name))
  print ("{:15}{}".format("Company:",company.strip()))
  print ("{:15}{}".format("Email:", email.strip()))
  print()
  #print ("{:20} {:15} {:20}".format(name, company, email))

file.close()