#Grade Calculator
#Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(below 60)
marks=int(input("Enter the marks of the student: "))
if(marks<60):
    print("The Student had got F grade...")
elif(marks>=60 and marks<=69):
    print("The Student had got D grade...")
elif(marks>=70 and marks<=79):
    print("The Student had got C grade...")
elif(marks>=80 and marks<=89):
    print("The Student had got B grade...")
elif(marks>=90 and marks<=100):
    print("The student had got A grade...")
else:
    print("Please enter the marks betweeen 0 and 100...")
#This program can handle minus marking too :)