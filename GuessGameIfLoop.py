from random import *


aRandomNumber = randint(1, 20)

numTries = 0

for numTries in range(3):
	guess = input("Guess a number between 1 and 20 (inclusive): ")

	if not guess.isnumeric():
		print("That's not a positive whole number, try again!")
	else:
		guess = int(guess) 
		if guess == aRandomNumber:
			print("That's right!")
			break
		else: 
			if guess < aRandomNumber:
				print("Guess higher!")
			else:
				print("Guess lower!")

