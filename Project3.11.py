import random
pot = int(input("Enter the amount of money to add to the pot: "))
maxPot = pot
count = 0
while pot > 0:
  dice = random.randint(1,12)
  if dice == 7:
    pot += 4
  else:
    pot -= 1
  if pot > maxPot:
    maxPot = pot
  count += 1
print("It took " + str(count) + " rolls to break player.")
print("The maximum amount of money in the pot was $" + str(maxPot))
