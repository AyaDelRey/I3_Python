valeur=[]
nombre=input("entrez un nombre:")
nombre=int(nombre)
valeur.append(nombre)
nombre=input("entrez un nombre:")
nombre=int(nombre)
valeur.append(nombre)
while valeur[-1]!=valeur[-2]:
    nombre=input("entrez un nombre:")
    nombre=int(nombre)
    valeur.append(nombre)
somme=sum(valeur)
print(somme)