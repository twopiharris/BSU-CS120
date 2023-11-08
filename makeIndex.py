""" utility program to create index.html from any directory """
import os

output = """
<!DOCTYPE HTML>
<html lang = "en-us">
<head>
  <title>List of demo files</title>
  <meta charset = "utf-8">
</head>

<body>
  <h1>List of Demo Files</h1>
  <ul>
"""
blackList = ("__pycache__", "dbinfo.txt")

files = os.listdir()
files.sort()
#remove files in blacklist
files = [x for x in files if x not in blackList]

for item in files:
  output += "    <li><a href = \"{}\">{}</a></li>\n".format(item, item)

output += """
  </ul>
</body>
</html>
"""

print(output)
#save to file
outFile = open("index.html", "w")
outFile.write(output)
outFile.close()