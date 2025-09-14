#7. Function with *args
#Problem: Write a function that takes variable number of arguments and returns their sum. 
def sum_all(*args): # asterisk(*) is imp
    return sum(args)
print(sum_all(1, 2, 3, 4, ))
print(sum_all(1, 2, 4, 99))
print(sum_all(1, 2, 4,99, 134, 123))