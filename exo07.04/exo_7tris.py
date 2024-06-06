from random import randint

def random_mot(longueur_mot, letters):
    mot = ''
    for _ in range(longueur_mot):
        index = randint(0, len(letters) - 1)
        lettre = letters.pop(index)
        mot += lettre
    return mot

letters=["a","e","v","t","d"]
longueur_mot = int(input("Entrez la longueur du mot: "))
mot_user = random_mot(longueur_mot, letters)
print("Mot:", mot_user)
