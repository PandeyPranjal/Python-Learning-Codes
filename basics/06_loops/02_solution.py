#2. Sum of Even Numbers
#Problem: Calculate the sum of even numbers up to a given number n.

num =int(input("Enter the range: "))
sum=0
for i in range(1, num+1):
    if(i%2==0):
        sum=sum+i
        
print(sum)