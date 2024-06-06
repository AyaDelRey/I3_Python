from random import randint

def random_mot():
    lettres_disponibles = ["a", "i", "l", "n", "o", "r", "s", "t"]
    mot = ''
    for _ in range(5):
        index = randint(0, len(lettres_disponibles) - 1)
        lettre = lettres_disponibles.pop(index)
        mot += lettre
    return mot

mot_user = random_mot()
print("Mot:", mot_user)
