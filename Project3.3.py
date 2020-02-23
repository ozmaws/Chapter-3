import random
import math
smaller = int(input("Enter a lower bound: "))
larger = int(input("Enter a upper bound: "))
userNumber = int(input("Enter a number between the upper and lower bounds: "))
while userNumber < smaller or userNumber > larger:
  print("Outside of bounds, choose a number within bounds.")
  userNumber = int(input("Enter a number between the upper and lower bounds: "))
count = 0
computerNumber = int(random.randint(smaller, larger))
print(str(computerNumber))
while count <= math.log((larger-smaller+1), 2):
  count+= 1
  correct = False
  if computerNumber == userNumber:
    print("You got it in " + str(count) + " tries, congratulations.")
    correct = True
    break
  elif computerNumber < userNumber:
    print("Too small")
    smaller = computerNumber+1
  elif computerNumber > userNumber:
    print("Too large")
    larger = computerNumber-1
  computerNumber = int(random.randint(smaller, larger))
  print(computerNumber)
if not correct:
  print("Computer not able to guess within given amount of tries.")
