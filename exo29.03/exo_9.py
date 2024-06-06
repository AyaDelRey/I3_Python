from random import randint

nombre1 =randint(1, 6)
nombre2 =randint(1, 6)
nombre3 =randint(1, 6)

print(nombre1)
print(nombre2)
print(nombre3)

while nombre1!=nombre3 and nombre3!=nombre2 and nombre1!=nombre2:
    nombre1 =randint(1, 6)
    nombre2 =randint(1, 6)
    nombre3 =randint(1, 6)
    print(nombre1)
    print(nombre2)
    print(nombre3)