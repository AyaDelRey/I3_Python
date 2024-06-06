password=input("Entrez votre mot de passe: ")
essai=2
while password!="Pyth0n" and essai>0:
    password=input("Entrez votre mot de passe: ")
    essai-= 1
if password=="Pyth0n":
    print("Mot de passe valide")
else:
    print("Mot de passe incorrect")
