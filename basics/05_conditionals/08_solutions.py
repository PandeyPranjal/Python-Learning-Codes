#8. Password Strength Checker
#Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria <6 chars(Weak), 6-10 chars (Medium), >10 chars(Strong)
password=input("Enter the password: ")
if len(password) <6:
    print("Weak Password")
elif len(password) <= 10:
    print("Medium Password")
else:
    print("Strong Passsword")
