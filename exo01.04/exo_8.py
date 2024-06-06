password="Pyth0n"
password_user=input("Entrez votre mot de passe: ")
essai=2
while password_user!=password and essai>0:
    password_user=input("Entrez votre mot de passe: ")
    essai-= 1
if password_user==password:
    print("Mot de passe valide")
else:
    print("Mot de passe incorrect")
