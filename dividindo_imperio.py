cidades = int(input())
grafo = {i:[] for i in range(1, cidades+1)}
for i in range(cidades-1):
    u, v = map(int, input().split())
    grafo[v].append(u)
    grafo[u].append(v)

#criação do vetor de grau dos vertices, para saber quem é folha e quem não é
grau_dos_vertices = []
soma_dos_adjacentes = []
fila_folha = []

#criação da função soma, para não usar sum() do python  
def somar(lista):
  soma = 0
  for valor in lista:
    soma += valor
  return soma

for x in grafo:
  grau_dos_vertices.append(len(grafo[x]))
  soma_dos_adjacentes.append(somar(grafo[x]))
  if len(grafo[x]) == 1:
    fila_folha.append(x)




#falta linkar o grafo com o grau das folhas, para poder conseguir fazer a fila
#a fila das folhas funciona pegando todos os vertices de grau 1 para deletar
#vertice de grau 1 = vertice com apenas 1 ligação
    

print(grau_dos_vertices,soma_dos_adjacentes,grafo,fila_folha
