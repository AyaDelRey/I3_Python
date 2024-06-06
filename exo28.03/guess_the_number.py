from random import randint

solution =randint(1, 10)
nombre = None
essai=3

while nombre != solution and essai > 0:
    nombre = input("Donne un nombre entre 1 et 10: ")
    essai-= 1
    nombre = int(nombre)
    if solution < nombre :
        print("Inférieur")
    elif solution > nombre :
        print("Supérieur")
    else:
        print("Bravo c'est correct")
if nombre != solution:
    print("Perdu le nombre exact est: "+str(solution))





