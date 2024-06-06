def ordre(mot):
    result=""
    for letter in mot:
        result = letter + result
        
    return result


m=input("Donne un mot: ")

print(ordre(m))


