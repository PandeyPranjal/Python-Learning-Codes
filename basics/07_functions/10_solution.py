#10. Recursive Function
#Problem: Create a recursive function to caluclate the factorial of a number.
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
    
num=int(input("Enter the number: "))
print(fact(num))