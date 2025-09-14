#9. List Uniqueness Checker
#Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
#items=["Apple", "Banana", "Orange", "Apple", "Mango"]
items=["Apple", "Banana", "Orange", "Apple", "Mango"]

unique_item=set()
for item in items:
    if item in unique_item:
        print(item," is not a unique item")
        break
    unique_item.add(item)