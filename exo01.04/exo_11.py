from random import randint

nombre1 =randint(0, 100)
nombre2 =randint(0, 100)
erreur=0


user_nombre=(input("Donnez la somme de "+str(nombre1)+"+"+str(nombre2)+"= "))
user_nombre=int(user_nombre)
while user_nombre!=nombre1+nombre2:
    user_nombre=(input("Donnez la somme de "+str(nombre1)+"+"+str(nombre2)+"= "))
    user_nombre=int(user_nombre)
    erreur=erreur+1
print("Erreur : "+str(erreur))
