#8. Function with **Kwargs
#Problem: Create a function that accepts any number of keyword arguments and prints them in the format 
#Key: value

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Pranjal", power="lazer")
print_kwargs(name="Azeem")
print_kwargs(name="Satish", power="lazy", enemy="Sleep")