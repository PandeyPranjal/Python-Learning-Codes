chai_types={"Masala": "Spicy", "Ginger": "Zesty", "Green": "Fresh"}
# print(chai_types)
# print(chai_types.get("Masala"))
# chai_types["Green"]= "Mild"
# print(chai_types)
# for chai in chai_types:
#     print(chai)


# for chai in chai_types:
#     print(chai, chai_types[chai])

# using items method to print keys and values using items method

# for key, value in chai_types.items():
#     print(key, value)


# if "Masala" in chai_types: 
#     print("Yes! I have masala chai")

# print(len(chai_types))      len() works to count the length as a key and value makes an item and it counts it 

# chai_types["Earl Grey"]="Citrus"
# print(chai_types)


#Pop method but requiremnt of key not like list method 
# chai_types.pop("Ginger")
# print(chai_types)

# chai_types.popitem()  as it pop last item
# print(chai_types)

# chai_types["Green"]="Fresh"
# print(chai_types)

# del chai_types["Green"]   Here is delete 
# print(chai_types)

# copied_chai=chai_types.copy()
# print(copied_chai)

# Now we are learning about dictionary inside dictonary

tea_shop={
    "chai":{
        "Masala": "Spicy", "Ginger": "Zesty"}, 
    "Tea":{
        "Green": "Mild", "Black": "Strong"
    }
}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])

# squared_num={x: x**2 for x in range(1, 11)}
# print(squared_num)

keys=["Masala", "Ginger", "Lemon"]
default_value="Delicious"
new_dict=dict.fromkeys(keys, default_value)
print(new_dict)