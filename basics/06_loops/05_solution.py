#5. Find the First Non-Repeated Character
#Problem: Given a string, find the first non-repeated character.

str=input("Enter the string: ")
for i in str:
    if str.count(i)==1:
        print("Non-repeated char is :", i)
        break