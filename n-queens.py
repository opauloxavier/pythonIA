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
		linha_secundaria = 0
		coluna_secundaria = 0
		soma = i + j

		if diferenca < 0:
			dif_coluna = diferenca * (-1)
		else:
			dif_linha = diferenca

		if soma > (self.tamanhoTabuleiro - 1):
			coluna_secundaria = self.tamanhoTabuleiro - 1
			linha_secundaria = soma - (self.tamanhoTabuleiro - 1)
		else:
			coluna_secundaria = soma

		print(linha_secundaria, coluna_secundaria)

		for x in range(self.tamanhoTabuleiro):
			for y in range(self.tamanhoTabuleiro):
				if (x == i or y == j) and self.tabuleiro[x][y] < 1:
					self.tabuleiro[x][y] = -1
				elif ((x == (i - linha + dif_linha)) and (y == (j - coluna + dif_coluna))):
					if self.tabuleiro[x][y] != 5:
						self.tabuleiro[x][y] = -1
					linha -= 1
					coluna -= 1
				if (x == linha_secundaria) and (y == coluna_secundaria):
					print(linha_secundaria, coluna_secundaria)
					if self.tabuleiro[x][y] != 5:
						self.tabuleiro[x][y] = -1
					linha_secundaria += 1
					coluna_secundaria -= 1


	def jogada(self, i, j):
		self.tabuleiro[i][j] = 5
		self.espacosRejeitados(i, j)
		print(self.tabuleiro)

class Arvore:
	def __init__(self, tamanho):
		self.raiz = No(tamanho)

node = No(6)
node.jogada(2, 3)
