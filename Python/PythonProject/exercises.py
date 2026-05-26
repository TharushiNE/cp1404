#Random width, given length, find the area

import random

length = int(input("Enter the length: " ))
width =  random.randint(1, length)
area = length * width
print ("Area of", length, "x", width, "is", area)