from random import randint
code=[]
lettres=["a", "b", "c", "d","e"]
def randlet():
    choice = randint(0,len(lettres)-1)
    return choice


for _ in range (5):
    code.append(lettres[randlet()])
    Strcode = "".join(code)
print(Strcode)