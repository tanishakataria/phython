chemistry= float(input("Enter the marks of chemistry"))
physics = float(input("Enter the marks of physics:"))
maths = float(input("Enter the marks of math:"))
marks =  {"Chemistry":chemistry,
    "Physics": physics,
     "Maths":maths
}
total = chemistry + physics + maths
average = total / 3

highest_subject = max(marks, key=marks.get)
highest_marks = marks[highest_subject]
print("Average marks",average)
print("Highest marks",highest_marks)
print("Highest subject marks",highest_subject)
