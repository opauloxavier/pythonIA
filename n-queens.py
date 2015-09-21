import numpy

sizeChest = 8

def start(sizeChest):
	return numpy.zeros((sizeChest,sizeChest))

def movement(chest,i,j):
	chest[i][j]=1

def  rejected_spot(i,j):

	print len(chest)
	line = i
	column = j

	for x in range(len(chest)):
		for y in range(len(chest)):
			if (x == i or y == j) and chest[x][y] != 1:
				chest[x][y] = -1
			if  (x == (i - line) and y = (j - column)) and  chest[x][y] != 1:
				chest[x][y] = -1
	print chest

def isPrincipalDiagonal(x, y, i, j):



def diagonais(i,j):
	loop=1
	
	for x in range(sizeChest):

		if(i+loop <sizeChest and i-loop >=0 and j-loop>=0 and j+loop<sizeChest):
			print(i+loop,j+loop)
			print(i-loop,j-loop)
			print(i-loop,j+loop)
			print(i+loop,j-loop)
			loop+=1	
	

chest = start(sizeChest)

#movement(chest,2,2)

#rejected_spot(2,2)

diagonais(2,2)
#print defineDiagonal(0,0)