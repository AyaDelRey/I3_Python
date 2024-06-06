from random import randint


CODE_LENGTH = 4
LETTERS = ["a", "b", "c", "d", "e", "f"]


code = []

for _ in range(CODE_LENGTH):
    index = randint(0, len(LETTERS) - 1)
    letter = LETTERS[index]
    code.append(letter)

guess = None
essai = 12

while guess != code  and essai > 0:

    print(f"Il vous reste {essai} essais")
    essai-=1

    guess = input("Entrez une proposition de " + str(CODE_LENGTH) + " lettres: ")
    while len(guess) != CODE_LENGTH:
        guess = input("Entrez une proposition de " + str(CODE_LENGTH) + " lettres: ")

    guess = list(guess)

    correct = []
    for i in range(CODE_LENGTH):
        if code[i] == guess[i]:
            correct.append(i)
    print(str(len(correct)) + " lettres bien placées.")

    mal_placé=[]
    # Vérification des lettres mal placées
    for i_guess in range(CODE_LENGTH):
        for i_code in range(CODE_LENGTH):
            if guess[i_guess] == code[i_code]:
                if i_code not in correct and i_guess not in correct:
                    if i_code not in mal_placé:
                        mal_placé.append(i_code)
                        break
    print(str(len(mal_placé)) + " lettres mal placées.")


if code== guess:
    print("Bravo!")
else:
    print(f"Désolé le code était {code}")