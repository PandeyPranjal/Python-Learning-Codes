# 1.Age Group Categrization:
# classify a person's age group: Child(<13), Teenageer(13-19), Adult(20-59), Senior(60+)

age=int(input("Enter the age: "))
if(age<=0):
    print("Age should be  greagter than zero")
elif (age<13 ):
    print("Child")
elif(age>=13 and age<=19):
    print("Teenager")
elif(age>=20 and age<=59):
    print("Adult")
else:
    print("Senior")
