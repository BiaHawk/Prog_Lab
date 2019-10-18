n = int(input())
alturas = [int(x) for x in input().split()]
copia = [x for x in alturas]
copia.pop()
minimo_valor_corte = 2

def somar(lista):
  soma = 0
  for valor in lista:
    soma += valor
  return soma

for y in copia:
    pico = somar(x > y and (index == 0 or alturas[index - 1] <= y) for index, x in enumerate(alturas)) + 1
    if minimo_valor_corte < pico:
        minimo_valor_corte = pico
        
print(minimo_valor_corte) 

    
