tables = [1,2,3,4,5,6,7,8,9,10]
def multiply(tables):
    for i in range(len(tables)):
        result=tables[i]*7
        print(str(tables[i])+"*7 = "+ str(result))

multiply(tables)

