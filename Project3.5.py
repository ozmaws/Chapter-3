init = int(input("Enter the initial population: "))
rate = int(input("Enter growth rate: "))
rateAcheived = int(input("Enter how many hours it will take to acheive growth rate: "))
time = int(input("Enter number of hours: "))
total = initial * (rate * (time/rateAcheived))
print("There will be approximately " + str(total) + " organsims after " + str(time) + " hours.")
