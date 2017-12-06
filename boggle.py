# A boggle board generator

from random import randint

# Define alphabet
alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Qu', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

# Get board dimensions
dimensions = ''
while dimensions == '':
	try:
		dimensions = int(input('Width and height? '))
	except:
		print('Please answer with an integer.')

# Generate a letter
def generateLetter():
	return alphabet[randint(0,25)]

# Display grid
for i in range(dimensions):

	for j in range(dimensions):
		letter = generateLetter()

		# Keep spacing consistent
		cell = letter.ljust(4)
		print(cell, end='')

	print('\n')
