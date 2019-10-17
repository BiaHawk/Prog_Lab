cidades = int(input())
grafo = {i:[] for i in range(1, cidades+1)}
grafoPontos = {i:1 for i in range(1, cidades+1)}
#grafoPontos é um dict para atribuir o grau ao vertice
for i in range(cidades-1):
    u, v = map(int, input().split())
    grafo[v].append(u)
    grafo[u].append(v)

#criação da fila das folhas, que é feita a partir do grau do vertice no grafo

while len(grafo) > 3:
  fila_folha = []
  for x in grafo: #laço que checa o grau e põe na fila folha
    if len(grafo[x]) == 1:
      fila_folha.append(x)


#varrendo a fila folha para "desfolhar" ela, ou seja, remover os nós folha
#
  for x in fila_folha:
#a medida que os vertices folhas são deletados, é atribuido o valor dele ao prox vertice
#ou seja, conta os grafos vertices até chegar no vertice central ou nos centrais
    grafoPontos[grafo[x][0]] += grafoPontos[x]
    for y in grafo:
      if x in grafo[y]:
        grafo[y].remove(x)
    del grafo[x]
    del grafoPontos[x]
    
  fila_folha = []

#trata os casos de centralidade dos vertices
  
if(len(grafoPontos) == 2):
  values = list(grafoPontos.values())
  var = values[0] - values[1]
  if var < 0:
    print(var * -1)
  else:
    print(var)
else:
  grau_dos_vertices = {}
  for x in grafo:
    grau_dos_vertices[x] = len(grafo[x])
  center = max(grau_dos_vertices, key=grau_dos_vertices.get)
  val1 = grafoPontos[grafo[center][0]] + grafoPontos[center] - grafoPontos[grafo[center][1]]
  val2 = grafoPontos[grafo[center][1]] + grafoPontos[center] - grafoPontos[grafo[center][0]]
  if(val1 < val2):
    print(val1)
  else:
    print(val2)
















        

