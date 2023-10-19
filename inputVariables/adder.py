"""
ask the user for two inputs x and y
add them together and report the sum
"""

#make an integer variable called x starting at 0
x = 0

#make an integer variable called y starting at 0
y = 0

#make an integer called sum will be sum of x and y
sum = 0

#ask for "X", put result in x
x = input("X: ")

#ask for "Y", put result in y
y = input("Y: ")

# convert x and y to integers
x = int(x)
y = int(y)

#calculate x + y, put in sum
sum = x + y

#output sum
print("{} + {} = {}".format(x, y, sum))
print("{} - {} = {}".format(x, y, x - y))
print("{} * {} = {}".format(x, y, x * y))
print("{} / {} = {}".format(x, y, x / y))
print("{} // {} = {}".format(x, y, x // y))
print("{} % {} = {}".format(x, y, x % y))

