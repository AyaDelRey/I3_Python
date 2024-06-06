from random import randint

def liste_entier(n):
    entier=[]
    for _ in range(n):
        nombre = randint(1, 6)
        entier.append(nombre)
    return entier

resultat=liste_entier(3)
print(resultat)