#7. Validate Input
#Problem: Keep asking the user for input until they enter a number between 1 and 10



while True:
    num=int(input("Enter the number: "))
    if( 1<= num <=10):
        print("Thankyou")
        break
    else:
        print("Invalid Number.. Try Again!")