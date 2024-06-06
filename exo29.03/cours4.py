vide=[]
mot=input("Entrez votre mot: ")
vide.append(mot)
print(vide)
while mot != "stop":
    mot=input("Entrez un autre mot: ")
    vide.append(mot)
print(vide)