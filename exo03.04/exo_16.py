mot = input("Entrez un mot : ")
lettre=list(mot)
voyelles = ["a", "e", "i", "o", "u", "y"]
nombre_voyelles = 0
for lettre in mot:
    if lettre in voyelles:
        nombre_voyelles += 1
print(nombre_voyelles)