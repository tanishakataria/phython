numbers =(input("Enter the numbers:"))
numbers = list(map(float,numbers.split()))
for num in numbers:
 if num%2==0:
  print(num ,"is even")
