from random import randint
def say_hello():
    salut=["Bonjour","Hello","Ola","Ciao"]
    choice = randint(0,len(salut)-1)
    print(salut[choice])


for _ in range (100):
    say_hello()


