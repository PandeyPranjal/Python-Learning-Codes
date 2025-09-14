#10. Pet Food Recommendation
#Problem: Recommend a type of pet food based on the pet's species and age. (Eg. Dog:<2 years-Puppy food, Cat:>5year-Senior cat food)
species=input("Enter the species of the animal(cat or dog: )").lower()
age=int(input("Enter the age: "))
if(species=="dog"):
    if(age<=2):
        print("puppy food should be provided")
    else:
        print("Can eat any type of eatables")
elif(species=="cat"):
    if(age<=2):
        print("Kitten and also kitten food")
    else:
        print("They can ear anything")
else:
    print("Choose b/w dogesh and cat")