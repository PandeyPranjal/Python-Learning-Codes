#4. Reverse a String
#Problem: Reverse a string using a loop
reversed_str=""
str=input("Enter a string: ")
for i in str:
    # reversed_str=reversed_str+i
    reversed_str=i+reversed_str
    
print(reversed_str)