first = int(input("Enter a positive number: "))
second = int(input("Enter a second positive number: "))
if first > second:
  larger = first
  smaller = second
else:
  larger = second
  smaller = first
while smaller != 0:
  print("")
  remainder = larger % smaller
  print("The remainder of dividing " + str(larger) + " by " + str(smaller) + " is " + str(remainder))
  larger = smaller
  smaller = remainder
  print("The larger number has been changed to " + str(larger) + " and the smaller number has been changed to " + str(smaller))

print("The smaller number is now 0")
print("The GCD is " + str(larger))
