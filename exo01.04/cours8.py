letters = ["a", "b", "c", "d", "e", "f"]
code=[]
code_length=4

while len(code)<code_length:
    from random import randint
    index =randint(0, len(letters)-1)
    select=letters[index]
    code.append(select)

print(code)