#Movie Ticket Pricing
#Movie tickets are priced based on age: $12 for adults(18 and over), $8 for children . Everyone gets a $2 discount on Wednesday

age=int(input("Enter the age: "))
day=input("Enter the day name: ").lower()
# ticket=0
if(age<18):
    # ticket= ticket+8
    ticket=8
elif(age>=18):
    # ticket= ticket+12
    ticket=12
if(day=="wednesday"):
    ticket=ticket-2
print("The price of the ticket is $",ticket)
