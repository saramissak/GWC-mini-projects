from random import *

mainCourse = ["steak", "pasta", "salad", "fondu"]
dessert = ["ice cream", "cake", "chocolate fountain"]
sides = ["mozzeralla sticks", "wings", "salad"]


aRandomIndexA = randint(0, len(mainCourse)-1)
print(mainCourse[aRandomIndexA])
#my more extra way for line 9: print(mainCourse[aRandomIndexA:aRandomIndexA + 1])

aRandomIndexB = randint(0, len(dessert)-1)
print(dessert[aRandomIndexB])
#print(dessert[aRandomIndexB:aRandomIndexB + 1])

aRandomIndexC = randint(0, len(sides)-1)
print(sides[aRandomIndexC])
#print(sides[aRandomIndexC:aRandomIndexC + 1])

print(aRandomIndexA)
