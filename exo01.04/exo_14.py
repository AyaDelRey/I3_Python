mot=input("Entrez votre mot: ")
count=1
while mot != "end":
    mot=input("Entrez un autre mot: ")
    count=count+1
    if mot[0]=="t":
        print(mot+"!!!")
print(count)