import numpy
import copy
import string
import nqueens

size = 6

class Matriz:
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

    #poe uma rainha no local indicado
    def jogada(self, i, j):
        self.tabuleiro[i][j] = 5
        self.espacosRejeitados(i, j)     


class Graph:
    def __init__(self):
        self.grafo = {}
        self.visited= None;
        for x,y in enumerate(string.uppercase):
            if (x==size):
                break
            else:
                self.grafo.update({y:set()})        


def profundidade(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        profundidade(graph, next, visited)
    return visited

def largura(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited
        

#cria matriz e faz jogadas
matriz=Matriz(6)
matriz.jogada(0,1)
matriz.jogada(1,3)
matriz.jogada(2,5)
matriz.jogada(3,0)
matriz.jogada(4,2)
matriz.jogada(5,4)

#print matriz.tabuleiro

busca = Graph()

meugrafo = {
		 'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])
         }

print profundidade(meugrafo,'A')
print largura(meugrafo,'A')

#data.update({'A':set(),'B':set(),'C':set()})

#	data.update({'D':set()})

#variavel.add(A)
#print data
#variavel['A'].update({'F'}) #adiciona coisas no set


