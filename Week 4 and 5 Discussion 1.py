##### Start Pseudocode####
#input budget
#output price of apples, cheese, and bread
#while runTotal < budget
#   input itemBuy
#   if itemBuy == -1
#       exit loop
#   endif
#   else if itemBuy == "apples"
#       input numApples
#       totalApples = totalApples + numApples
#   endif
#   else if itemBuy == "cheese"
#       input numCheese
#       totalCheese = totalCheese + numCheese
#       total = total + (price of cheese * numcheese)
#   endif
#   else if itemBuy == "bread"
#       input numBread
#       totalBread = totalBread + numBread
#       total = total + (price of bread * numBread)
#   endif
#endwhile
#output total, totalApples, totalCheese, and totalBread
##### End Pseudocode #####

#Set Constants
Apples = 1.00 #constant price for apples
Cheese = 1.00 # """"""""""""""""" cheese
Bread = 2.00 #""""""""""""""""""" bread
count = 0 #tracks how many the person wants to buy
appleCount = 0 #count of apples
cheeseCount = 0 #count of cheese
breadCount = 0 #count of bread
total = 0 #tracks total items
budgetLeft = 0 #tracks how much money is left to spend
item = "" #tracks the item

#beginning of program
budget = float(input("Please input your lunch budget: "))
print("Apples are $1.00")
print("Cheese is $1.00")
print("Bread is $2.00")

#beginning of nestled loop
while total < budget:
    cancel = False #tracks if the user cancels the program at any time for any item
    item = input("Enter the type of item to buy, or enter -1 to exit: ")
    if item == "-1": #sentinel value to exit and displays budget
        break
    elif item.lower() == "apples": #this function will convert string item to lowercase for all items 
        count = int(input("Enter how many apples: "))
        if total + (Apples * count) > budget: #checks if this will go over budget
            decision = input("This will set you over budget, enter 'yes' if this is okay or 'no' if it is not to cancel: ")
            if decision.lower() == "yes": #will exit loop since over budget
                appleCount = appleCount + count
                total = total + (Apples * count)
                break
            else: #if the user wants to not go over budget this will cancel the addition
                cancel = True
                print("Cancelled addition.")
                print("You have $" + ('%2' % budgetLeft) + " left in your lunch budget.") #the '2.f%' prompt ensures 2 decimals 
        else: #if it is not over budget the 'count' apples are added to the list
            appleCount = appleCount + count
            total = total + (Apples * count)
    elif item.lower() == "cheese": #all comments are the same for cheese and bread in the rest of the program
        count = int(input("Enter how much cheese: "))
        if total + (Cheese * count) > budget:
            decision = input("This will set you over budget, enter 'yes' if this is okay or 'no' if it is not to cancel: ")
            if decision.lower() == "yes":
                cheeseCount = cheeseCount + count
                total = total + (Cheese * count)
                break
            else:
                cancel = True
                print("Cancelled addition.")
                print("You have $" + ('%2' % budgetLeft) + " left in your lunch budget.")
        else:
            cheeseCount = cheeseCount + count
            total = total + (Cheese * count)
    elif item.lower() == "bread":
        count = int(input("Enter how much bread: "))
        if total + (Bread * count) > budget:
            decision = input("This will set you over budget, enter 'yes' if this is okay or 'no' if it is not to cancel: ")
            if decision.lower() == "yes":
                breadCount = breadCount + count
                total = total + (Bread * count)
                break
            else:
                cancel = True
                print("Cancelled addition.")
                print("You have $" + ('%2' % budgetLeft) + " left in your lunch budget.")
        else:
            breadCount = breadCount + count
            total = total + (Bread * count)
    budgetLeft = budget - total
    if total < budget and not cancel:
        print("You currently have " + str(appleCount) + " apple(s), " + str(cheeseCount) + " unit(s) of cheese " + str(breadCount) + " unit(s) of bread for a total of $" + ('%2.f' % total))
        print("Your budget currently stands at $" + ('%.2f' % budgetLeft))
print("Your total items are: ")
print(str(appleCount) + " apple(s)")
print(str(cheeseCount) + " units(s) of cheese")
print(str(breadCount) + " units(s) of bread")
if total > budget: #the next three lines will indicate the response from the math stating a response with over, under, or at the budget that was input 
    overBudget = total - budget
    print("Your total is $" + ('%.2f' % total) + " which is $" + ('%.2f' % overBudget) + " over budget.")
elif total < budget:
    underBudget = budget - total
    print("Your total is $" + ('%.2f' % total) + " which is $" + ('%.2f' % underBudget) + " under budget.")
else:
    print("Your total is $" + ('%.2f' % total))
