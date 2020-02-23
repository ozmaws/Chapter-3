initHeight = float(input("Enter the initial height: "))
numBounces = int(input("Enter the number of allowed bounces: "))
totalDist = 10 + (initHeight*2)
count = 1
bounceIndex = initHeight / 10
newHeight = bounceIndex * initialHeight
while count < numBounces:
  totalDist = totalDist + (newHeight*2)
  newHeight = bounceIndex * newHeight
  count += 1
totalDist = totalDist + newHeight
print("The ball will travel " + str(totalDist) + "feet after " + str(numBounces) + " bounce(s).")
