#6. Factorial Calculator
#Problem: Compute the factorial of a number using a while loop


n=int(input("Enter the number: "))
fact=1
# for i in range(1, n+1):
#     fact=fact*i
# print(fact)

while n>0:
    fact=fact*n
    n=n-1
    
print("The factorial of the number is : ", fact)