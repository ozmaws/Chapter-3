count = 0
add = False
result = 0
denom = 3
iterations = int(input("Enter the number of iterations: "))
while count < iterations:
  if result == 0:
    result = 1
    count += 1
    continue
  if add == True:
    result = result + (1/denom)
    add = False
  else:
    result = result - (1/denom)
    add = True
  denom = denom + 2
  count+= 1
print("Doing " + str(iterations) + " iterations results in " + str(result))
