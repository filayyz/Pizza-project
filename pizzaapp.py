# PIZZA SIZE SELECTION

# Print a greet message and ask user what size pizza they would like
print("""Welcome to Pizzazz!
What size pizza would you like?""")

# This will prompt the user to input a letter for the desired pizza size
sizeChoice = input("Please enter S for Small, M for Medium, L for Large:")

# Ensure that lowercase inputs are also accepted and not limited to uppercase
size = sizeChoice.upper()

if size == "S":
    print("You selected a SMALL pizza.")
elif size == "M":
    print("You selected a MEDIUM pizza.")
elif size == "L":
    print("You selected a LARGE pizza.")
else:
    print("That size is not available.")



# TOPPING SELECTION

# This will prompt the user to choose if they want PEPPERONI as a topping
toppingChoice1 = input("Would you like PEPPERONI? (Y/N):")
topping1 = toppingChoice1.upper() # Ensure that lowercase inputs are also accepted and not limited to uppercase

if topping1 == "Y":
    print("Great, PEPPERONI ADDED!")
elif topping1 == "N":
    print("No PEPPERONI selected.")
else:
    print("Invaild selection, default to NO PEPPERONI.") # Have an else statement to handle invalid inputs

# This will prompt the user to choose if they want EXTRA CHEESE as a topping
toppingChoice2 = input("Would you like EXTRA CHEESE? (Y/N):")
topping2 = toppingChoice2.upper() # Ensure that lowercase inputs are also accepted and not limited to uppercase

if topping2 == "Y":
    print("Great, EXTRA CHEESE ADDED!")
elif topping2 == "N":
    print("No EXTRA CHEESE selected.")
else:
    print("Invalid selection, default to NO EXTRA CHEESE.") 



# PRICE CALCULATIONS

def calculateTotal(sizeChoice, hasPepperoni, hasExtraCheese):

    # Store all prices in dictionaries
    basePrices = {"S" : 15.00, "M" : 20.00, "L" : 25.00}
    pepperoniPrices = {"S" : 2.00, "M" : 3.00, "L" : 3.00}
    
    #Added invalid input handling, will return 0
    if sizeChoice not in basePrices:
        return 0
    # This will isolate the individual cost and giving each a starting value of 0
    baseCost = basePrices[sizeChoice]
    pepperoniCost = 0.00
    cheeseCost = 0.00

    # Add topping prices to the starting value of 0
    if hasPepperoni == "Y":
        pepperoniCost = pepperoniPrices[sizeChoice]
    if hasExtraCheese == "Y":
        cheeseCost = 1.00
    
    # Then calculate final total at the end of the function
    total = baseCost + pepperoniCost + cheeseCost

    return total, baseCost, pepperoniCost, cheeseCost # This will return each individual cost/value to the main program



# ORDER SUMMARY

finalTotal, baseCost, pepperoniCost, cheeseCost = calculateTotal(size, topping1,topping2)

print("---ORDER SUMMARY---")# Ensure order summary is easy for user to locate

if finalTotal > 0:
    print(f"Base Pizza ({size}): $" + format(baseCost, ".2f"))

    if pepperoniCost > 0:
        print(f"Pepperoni: $" + format(pepperoniCost, ".2f"))
    if cheeseCost > 0:
        print(f"Extra Cheese: $" + format(cheeseCost, ".2f"))
    
    print("-------------------") # Visual separator for organization

    print(f"Your total comes out to $" + format(finalTotal, ".2f"))# Need to format the finalTotal separately to eliminate space between $ and integer
    print("Thank you for choosing Pizzazz!")
else:
    print("Order cannot be completed.")
