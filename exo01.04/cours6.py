numbers=[1,2,3,4,5,1,2,3,4,5]
print(numbers)
user_number=input("Entrez un nombre entre 1 et 5: ")
user_number=int(user_number)
numbers.remove(user_number)
print(numbers)