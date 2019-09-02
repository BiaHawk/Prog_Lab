passos = [x for x in input().split()]
metros = 0
for x in range(len(passos)):
    if "F" in passos[x]:
        metros +=1
    if "T" in passos[x]:
        metros -=1


if metros <= -1:
    metros = metros*(-1)


print(metros)
