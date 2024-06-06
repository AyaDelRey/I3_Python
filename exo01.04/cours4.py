mots=[]
mot=input("Entrez votre mot: ")
mots.append(mot)
while mot != "stop":
    mots.append(mot)
    mot=input("Entrez un autre mot: ")
print(mots)