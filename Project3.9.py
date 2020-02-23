total = 0
count = 0
while True:
  num = input("Enter a number or press enter to exit: ")
  if num == "":
    break
  else:
    num = int(num)
    total = total + num
    count += 1
if count == 0:
  print("No numbers were entered.")
else:
  print("The sum of the numbers is " + str(total) + " and the average is " + str(total/count))
