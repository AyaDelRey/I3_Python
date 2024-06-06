tables = [1,2,3,4,5,6,7,8,9,10]
numbers=[7]

def table():
    for table in tables:
        for number in numbers:
            number_final=number*table
            return number_final

print(table())