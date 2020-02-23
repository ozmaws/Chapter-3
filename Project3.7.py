from PrettyTable import PrettyTable
salary = int(input("Enter the starting salary: "))
percRaise = (float(input("Enter the percentage increase in teacher's salary: "))/100)
numYears = int(input("Enter the number of years: "))
print("")
count = 0
table = PrettyTable(['Years of Experience', 'Salary'])
while count-1 < numYears:
  table.add_row([count, ('%.2f' % salary)])
  salary = salary + (salary * percRaise)
  count += 1
print(table)
