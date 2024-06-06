mots=[]
mot=input("Entrez votre mot: ")
while mot != "stop":
    place=input("Index dans la liste: ")
    place=int(place)
    mots.insert(place,mot)
    mot=input("Entrez un autre mot: ")
print(mots)