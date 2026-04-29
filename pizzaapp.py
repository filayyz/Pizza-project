#Print a greet message and ask user what size pizza they would like
print("""Welcome to Pizzazz!
What size pizza would you like?""")

#This will prompt the user to input a letter for the desired pizza size
sizeChoice = input("Please enter S for Small, M for Medium, L for Large:")

#Ensure that lowercase inputs are also accepted and not limited to uppercase
size = sizeChoice.upper()

if size == "S":
    print("You selected a SMALL pizza.")
elif size == "M":
    print("You selected a MEDIUM pizza.")
elif size == "L":
    print("You selected a LARGE pizza.")
else:
    print("That size is not available.")



#Topping Selection

#This will prompt the user to choose if they want PEPPERONI as a topping
toppingChoice1 = input("Would you like PEPPERONI? (Y/N):")
topping1 = toppingChoice1.upper() #Ensure that lowercase inputs are also accepted and not limited to uppercase

if topping1 == "Y":
    print("Great, PEPPERONI ADDED!")
elif topping1 == "N":
    print("No PEPPERONI selected.")
else:
    print("Invaild selection, default to NO PEPPERONI.") #Have an else statement to handle invalid inputs

#This will prompt the user to choose if they want EXTRA CHEESE as a topping
toppingChoice2 = input("Would you like EXTRA CHEESE? (Y/N):")
topping2 = toppingChoice2.upper() #Ensure that lowercase inputs are also accepted and not limited to uppercase

if topping2 == "Y":
    print("Great, EXTRA CHEESE ADDED!")
elif topping2 == "N":
    print("No EXTRA CHEESE selected.")
else:
    print("Invalid selection, default to NO EXTRA CHEESE.") 
