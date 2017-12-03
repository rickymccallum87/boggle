# A boggle board generator

from random import randint

# Define alphabet
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Qu', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Get board dimensions
dimensions = int(input('Width and height? '))

# Generate a letter
def generateLetter():
	return alphabet[randint(0,25)]

# Display grid
for i in range(dimensions):
	for j in range(dimensions):
		letter = generateLetter()

		# Keep spacing consistent
		cell = letter.ljust(3)
		print(cell, end='')
	print('')
