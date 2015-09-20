import numpy

sizeChest=8

def start(sizeChest):
	return numpy.zeros((sizeChest,sizeChest))

def movement(chest,i,j):
	chest[i][j]=1

def rejected_Spots(i,j):
	xmax=sizeChest-1
	ymax=sizeChest-1

	for x,y in enumerate(chest):
		print float(x)==y[x]



chest = start(sizeChest)

movement(chest,0,0)

rejected_Spots(0,0)
