mot=None
count=0
while mot != "end":
    mot=input("Entrez un autre mot: ")
    count=count+1
    if len(mot)>0 and mot[0]=="t":
        print(mot+"!!!")
print(count)