#3. Multiplication Table Printer
#Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

n=int(input("Enter the number: "))
mul=1
for i in range(1, 11):
    #skip the if block if u want the full table
    if i==5:
        continue
    # mul=n*i
    # print(mul)
    print(n, "x", i, "=", n*i)