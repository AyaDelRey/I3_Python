letters = ["a", "b", "c", "d", "e", "f"]
code=[]
code_length=4
correct_letters=[]

for i in range (code_length):
    from random import randint
    index =randint(0, len(letters)-1)
    select=letters[index]
    code.append(select)

print("Code"+str(code))
guess=None

while code!=guess:
    guess=input("Devine un code de " + str(code_length) + " lettres: ")
    while len(guess)<code_length:
        guess=input("Devine un code de " + str(code_length) + " lettres: ")

    guess=list(guess)
    print("Essai:" +str(guess))

    for j in range (code_length):
                for k in range(code_length):
                    if code[j]==guess[j]:
                        correct_letters.append(guess[j])
                        print("correct letter" + str(correct_letters))
                        print(len(correct_letters))
                        
