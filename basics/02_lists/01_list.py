tea_varieties=["Black", "Green", "Oolong", "White"]
# print(tea_varietes)
# print(tea_varietes[0])
# print(tea_varietes[-1])
# print(tea_varietes[1:3])
# tea_varietes[2]="Herbal"



# print(tea_varieties)
# for chaay in tea_varieties:
#     print(chaay)
    
# if "Masala" in tea_varieties:
#     print("I have masala tea")
# else:
#     print("naah")
#     tea_varieties.append("Masala")
# print(tea_varieties)


# print(tea_varieties)
tea_varieties.pop()
print(tea_varieties)
tea_varieties.remove("Green")
print(tea_varieties)
tea_varieties.insert(1, "Masala")
print(tea_varieties)

tea_varieties_copy=tea_varieties.copy()
print(tea_varieties_copy)


#List Comprehension

squared_num=[x**2 for x in range (10)]
print(squared_num)

cube_num=[x**3 for x in range(10)]
print(cube_num)