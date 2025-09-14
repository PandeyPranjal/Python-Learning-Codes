#6. Transportation Mode Selection
#Problem: Choose a mode of transportation based on the distance( e.g. <3km:walk, 3-15km: Bike, >15km: Car)
dist=int(input("Enter the distance in km: "))
if(dist<=0):
    print("Distance should be greater than zero")
elif(dist<3 and dist>=1):
    print("Start Walking dude!")
elif(dist>=3 and dist<=15):
    print("Find a bike")
else:
    print("Find a Car ")