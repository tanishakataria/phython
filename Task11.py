English = float(input("Enter the marks of english"))
math = float(input("Enter the marks of math"))
science = float(input("Enter the marks of science"))
marks = {
    'English': English,
    'Math': math,
    'Science': science
}
total = English+math+science
average = total/3
percentage = (total/300)*100
print("Marks",marks)
print("Total average",average)
print("Percentage",percentage)
