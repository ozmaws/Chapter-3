#ask for numbers
firNum = int(input("Please enter a number: "))
secNum = int(input("Please enter a second number: "))

#loop logic
if firNum > secNum:
    lrgNum = firNum
    smlNum = secNum
else:
    lrgNum = secNum
    smlNum = firNum
while smlNum > 0:
    remainder = lrgNum % smlNum
    lrgNum = smlNum
    smlNum = remainder
print("The GCD of " + str(firNum) + " and " + str(secNum) + " is " + str(lrgNum))
