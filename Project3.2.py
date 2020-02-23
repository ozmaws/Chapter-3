fstSide = int(input("Length of the first side: "))
scndSide = int(input("Length of the second side: "))
thrdSide = int(input("Length of the third side: "))
if ((fstSide**2 + scndSide**2) == thrdSide**2):
  print("Right triangle.")
elif ((scndSide**2 + thrdSide**2) == fstSide**2):
  print("Right triangle.")
elif ((fstSide**2 + thrdSide**2) == scndSide**2):
  print("Right triangle.")
else:
  print("Not a right triangle.")
