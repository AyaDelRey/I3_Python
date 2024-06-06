lettres = ['a','b','c','d','e','f']
nombre = input("Donne un nombre entre 1 et 6: ")
nombre=int(nombre)
while nombre!=None and nombre>len(lettres) or nombre<0:
    nombre = input("Donne un nombre entre 1 et 6: ")
    nombre =int(nombre)
print(lettres)
print(lettres[:nombre])
print(lettres[nombre:])
