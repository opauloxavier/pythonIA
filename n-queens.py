import numpy
import copy

class No:
	def __init__(self, tamanho):
		self.tamanhoTabuleiro = tamanho
		self.tabuleiro = numpy.zeros((tamanho, tamanho))
		self.filhos = []

	#anula as diagonais, linhas e colunas da rainha
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
					if self.tabuleiro[x][y] != 5:
						self.tabuleiro[x][y] = -1
					linha_secundaria += 1
					coluna_secundaria -= 1

	#põe uma rainha no local indicado
	def jogada(self, i, j):
		self.tabuleiro[i][j] = 5
		self.espacosRejeitados(i, j)

class Arvore:
	def __init__(self, tamanho):
		self.raiz = No(tamanho)

	#faz os filhos da raiz, usar copy.deepcopy para fazer passagem de valor
	#funcao generica, tem que generalizar 
	def possibilidadesRaiz(self):
		for x in range(self.raiz.tamanhoTabuleiro):
			for y in range(self.raiz.tamanhoTabuleiro):
				no = copy.deepcopy(self.raiz)
				no.jogada(x, y)
				self.raiz.filhos.append(no)
		print(len(self.raiz.filhos))

	#conta e retorna quantos vazios tem no tabuleiro, entrada eh um no
	def vazios(self, no):
		vazios = 0
		for x in range(no.tamanhoTabuleiro):
			for y in range(no.tamanhoTabuleiro):
				if no.tabuleiro[x][y] == 0:
					vazios += 1
		return vazios


tree = Arvore(4)
tree.possibilidadesRaiz()
print(tree.vazios(tree.raiz.filhos[0]))
