from prettytable import PrettyTable
#Set constants
DOWN_PAYMENT_RATE = 0.1
ANNUAL_INTEREST_RATE = 0.12
MONTHLY_PAYMENTS_RATE = 0.05
month = 1
table = PrettyTable(['Month', 'Current Balance Owed', 'Interest Owed', 'Principal Owed', 'Monthly Payment', 'Remaining Balance'])
price = float(input("Please enter a purchase price: "))
adjustedPrice = price - (price*DOWN_PAYMENT_RATE)
MONTHLY_PAYMENTS = MONTHLY_PAYMENTS_RATE * adjustedPrice
interestOwed = adjustedPrice * (ANNUAL_INTEREST_RATE/12)
principalOwed = (MONTHLY_PAYMENTS) - (interestOwed)
remainingBalance = adjustedPrice - MONTHLY_PAYMENTS
table.add_row([month, ("$" + '%.2f' % adjustedPrice), ("$" + '%.2f' % interestOwed), ("$" + '%.2f' % principalOwed), ("$" + '%.2f' % MONTHLY_PAYMENTS), ("$" + '%.2f' % remainingBalance)])
while int(remainingBalance) > 0:
  month += 1
  currentBalance = remainingBalance
  interestOwed = currentBalance * (ANNUAL_INTEREST_RATE/12)
  principalOwed = MONTHLY_PAYMENTS - interestOwed
  remainingBalance = remainingBalance-MONTHLY_PAYMENTS
  table.add_row([month, ("$" + '%.2f' % currentBalance), ("$" + '%.2f' % interestOwed), ("$" + '%.2f' % principalOwed), ("$" + '%.2f' % MONTHLY_PAYMENTS), ("$" + '%.2f' % remainingBalance)])
print("\nDown Payment of $" + str(('%.2f' % (price*DOWN_PAYMENT_RATE))) + " required immediately.\n")
print(table)
