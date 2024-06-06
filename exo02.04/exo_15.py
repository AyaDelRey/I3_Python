number= input("Nombre entre 1 et 100: ")
number=int(number)
somme = 0
while number>100 or number<1:
    number= input("Nombre entre 1 et 100: ")
    number=int(number)
for i in range(1, number + 1):
        somme = somme+i
print(somme)