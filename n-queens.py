import numpy

class No:
	def __init__(self, tamanho):
		self.tamanhoTabuleiro = tamanho
		self.tabuleiro = numpy.zeros((tamanho, tamanho))

	def espacosRejeitados(self, i, j):
		linha = i
		coluna = j
		diferenca = i - j
		dif_linha = 0
		dif_coluna = 0

		if diferenca < 0:
			dif_coluna = diferenca * (-1)
		else:
			dif_linha = diferenca

		for x in range(self.tamanhoTabuleiro):
			for y in range(self.tamanhoTabuleiro):
				if (x == i or y == j) and self.tabuleiro[x][y] < 1:
					self.tabuleiro[x][y] = -1
				elif ((x == (i - linha + dif_linha)) and (y == (j - coluna + dif_coluna))):
					if self.tabuleiro[x][y] != 5:
						self.tabuleiro[x][y] = -1
					linha -= 1
					coluna -= 1


	def jogada(self, i, j, valor):
		self.tabuleiro[i][j] = valor
		self.espacosRejeitados(i, j)

class Arvore:
	def __init__(self, tamanho):
		self.raiz = No(tamanho)

node = No(8)
node.jogada(2, 3, 5)
