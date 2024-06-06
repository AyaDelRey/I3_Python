numbers=[1,2,3,4,5]
print(numbers)
count=len(numbers)
while count!=0:
    removed=numbers.pop(0)
    print(removed)
    print(numbers)