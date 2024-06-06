from random import randint

nombre1 =randint(1, 6)
nombre2 =randint(1, 6)
nombre3 =randint(1, 6)
print(nombre1,nombre2,nombre3)


while nombre1!=nombre2  or nombre3!=nombre1:
    nombre1 =randint(1, 6)
    nombre2 =randint(1, 6)
    nombre3 =randint(1, 6)
    print(nombre1,nombre2,nombre3)
