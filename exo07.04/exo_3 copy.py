
def multiply(number):
    tables = [1,2,3,4,5,6,7,8,9,10]
    for i in range(len(tables)):
        result=tables[i]*number
        print(str(tables[i])+"*" +str(number) + " = "+ str(result))

multiply(6)



