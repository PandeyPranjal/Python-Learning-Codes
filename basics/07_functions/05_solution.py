#5. Defautl Parameter Value
#Problem: Write a function that greets a user. if no name is provided, it should greet with a default name.

def greet(name="Pranjal"):
    return "Hello, " + name + "!"

print(greet("User"))
print(greet())