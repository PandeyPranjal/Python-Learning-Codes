#4. Fruit Ripeness Checker
# Determine if a fruit is ripe, overripe, or unripe based on its color. (eg.Banana:Green-Unripe, Yellow-Ripe, Brown -Overripe)
color=input("Enter the color of the fruit: ").lower()
quality=None
if(color=="green"):
    quality="Unripe"
elif(color=="yellow"):
    quality="Ripe"
elif(color=="brown"):
    quality="Overripe"
else:
    print("Choose b/w Yellow, Green and Brown")
print(quality)