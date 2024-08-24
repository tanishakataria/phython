number = 10
numbers = list(map(int,input("Enter the numbers seperated ny commas:").split(',')))
print("original list",numbers)
i =0
while i < len(numbers):
    if numbers[i] <= number:
        print("removed number:",numbers[i])
        numbers.pop(i)
    else:
       i+=1
    print("numbers left",numbers)
