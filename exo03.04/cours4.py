# page 201

from random import randint


def random_letter(taille):

    word = ""
    possibilities = ["a", "h", "k", "o", "n","s","t"]

    for _ in range(taille):
        
        index = randint(0, len(possibilities) - 1)
        letter = possibilities[index]
        word += letter

    return word


t=int(input("Combien de lettres? : "))



print(random_letter(t))