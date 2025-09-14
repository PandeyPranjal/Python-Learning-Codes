#8.Prime Number Checker
num=int(input("Enter the number: "))
if num>1:
    for i in range(2, num):
        if num%i==0:
            print("Number is not prime")
            break
        else:
            print(num, "is  a prime number")
else:
    print(num, "is not a prime no")