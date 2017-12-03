# A boggle board generator

import random

# Define alphabet
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Qu', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Get board dimensions
dimensions = int(input('Width and height? '))

# Generate a letter
def generateLetter():
	return alphabet[random.randint(0,25)]

# Display grid
for i in range(dimensions):
	for j in range(dimensions):
		letter = generateLetter()

		# Keep spacing consistent
		if letter == 'Qu':
			print(letter, end='')	
		else:
			print(letter, end=' ')
	print('')
