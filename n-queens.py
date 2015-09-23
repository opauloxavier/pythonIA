import numpy

sizeChest = 8

def start(sizeChest):
	return numpy.zeros((sizeChest,sizeChest))

def movement(chest,i,j):
	chest[i][j] = 5

def  rejected_spot(i,j):

	print len(chest)
	line = i
	column = j

	for x in range(len(chest)):
		for y in range(len(chest)):
			if (x == i or y == j) and chest[x][y] != 5:
				chest[x][y] = -1
			elif  ((x == (i - line)) and (y == (j - column))):
				if chest[x][y] != 5:
					chest[x][y] = -1
				line -= 1
				column -= 1
	print chest

chest = start(sizeChest)

movement(chest,4,3)

rejected_spot(4,3)

#diagonais(2,2)
#print defineDiagonal(0,0)