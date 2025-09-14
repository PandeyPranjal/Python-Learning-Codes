#4. Function Returning Mutiple Values
#Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math
def circle_stats(radius):
    area=  math.pi * radius ** 2
    circumference= 2 * math.pi * radius
    return (area, circumference)

radius= int (input("Enter the radius: "))

a, c=circle_stats(radius)
print("area: ",a , "circumference: ", c)