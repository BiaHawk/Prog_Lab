n = int(input())
alturas = [int(x) for x in input().split()]
maximo_papel = 2 #2 é o valor minimo de papeis que o pior corte pode ter

#iterar por todas as alturas e adiciona 1 ao contador quando a altura superar a altura de corte
for y in alturas[:-1]:
  contador = 1
  for x in range(len(alturas)):
    if alturas[x] > y:
      if x == 0 or alturas[x-1] <= y:
        contador +=1
  
  if maximo_papel < contador:
      maximo_papel = contador
        
print(contador) 
