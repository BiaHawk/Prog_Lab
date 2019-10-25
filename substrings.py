teste = "paula"

def all_substrings(string):
    if len(string) == 0:
        return ['']
    substrings = all_substrings(string[1:])
    return [(string[0] + substr) for substr in substrings] + substrings

print(all_substrings(teste))

############RAZOAVELMENTE FUNCIONANDO O PRIMEIRO EXEMPLO################

def all_substrings(string, n): 
    for x in range(n): 
        for len in range(x+1,n+1): 
            print(string[x: len])

string = "paula"
all_substrings(string,len(string)) 

###############FUNCIONANDO TOTALMENTE###########################

