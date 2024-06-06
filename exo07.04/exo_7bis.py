from random import randint

def random_mot(longueur_mot):
    lettres_disponibles = ["a", "i", "l", "n", "o", "r", "s", "t"]
    mot = ''
    for _ in range(longueur_mot):
        index = randint(0, len(lettres_disponibles) - 1)
        lettre = lettres_disponibles.pop(index)
        mot += lettre
    return mot

longueur_mot = int(input("Entrez la longueur du mot: "))
mot_user = random_mot(longueur_mot)
print("Mot:", mot_user)
