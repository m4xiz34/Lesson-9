print("Select a country that coresponse with your preference on food:")
print("1. Chinese")
print("2. Indian")

choice = int(input("Enter your answer using the number adjacent to it:  "))

if choice == 1:
    print("Select the given options:")
    print("1. Chowmein.")
    print("2. Dumplings. ")
    print("3. Mapo tofu. ")

    choice2 = int(input("Enter your answer using the number adjacent to it:"))
    if choice2 == 1:
       print("You have selected Chowmein. Thank you for your order.")
    elif choice2 == 2:
           print("You have selected Dumplings. Thank you for your order.")
    else:
        print("You have selected Mapo tofu. Thank you for your order.") 
elif choice == 2:
    print("Select the given options:")
    print("1. Biryani.")
    print("2. Idli Sambur. ")
    print("3. Dosa. ")
    
    choice3 = int(input("Enter your answer using the number adjacent to it:  "))
    if choice3 == 1:
        print("You have selected Biryani. Thank you for your order.")
    elif choice3 == 2: 
        print("You have selected Idli Sambur. Thank you fo your order.")
    else:
        print("You have selected Dosa. Thank you for your order.")
else:
    print("Invalid input/choice provided. Restart the program and try again.")
