num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))
operation = (input("Enter the operation (+,-,*,/) :"))
if operation == "-":
    result = num1-num2
elif operation =="*":
    result = num1*num2
elif operation =="/":
    if num2!=0:
     result = num1/num2
    else:
     result = "error divison"
elif operation == "+":
    result = num1-(-num2)
else:
    result = "invalid operation"

print("Result:",result)
