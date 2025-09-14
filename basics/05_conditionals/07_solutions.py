#7. Coffee Customization
#Problem: Customize a coffee order: "Small", "Medium" or "Large" with an  option for "Extra Shot" of expresso.
size=input("Enter the size of the drink(Small, Medium, large)").lower()
shot=input("Do you want an extra shot(yes/no)").lower()
if size in ["small", "medium", "large"]:
    order=f"{size.capitalize()} coffee "
    if shot=="yes":
        order+= " with extra shot of expresso"
    print("Your Order" , order)
else:
    print("Invlaid choice")