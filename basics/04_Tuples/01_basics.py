# tea_types=("Black", "Green", "Oolong")
# print(tea_types)
# print(tea_types[0])
# print(tea_types[1:])
# print(tea_types[-1])

# tuple is immutable that's why we can't assign values later

# more_tea=("Herbal", "Earl Grey")
# all_tea=tea_types + more_tea
# print(all_tea)

# if "Green" in all_tea:
#     print("I have Green Tea")

# more_tea=("Herbal", "Earl Grey", "Herbal")
# print(more_tea.count("Herbal"))


#Tuple Unpacking

tea_types=('Black', 'Green', 'Oolong')
(black, green, oolong)=tea_types
print(black) 