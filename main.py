import replit

print('\nCalculator v1')
a = int(input('\nEnter number: '))

replit.clear()
print('\nCalculator v1')
print('\nEnter a logical operator. (`+, -, *, /`)')
operation = input('\n')

replit.clear()
print('\nCalculator v1')
b = int(input('\nPlease enter your second number: '))

# Calculating process

if operation == '+':
  print("\n{}".format(a+b))
  
if operation == '-':
  print("\n{}".format(a-b))

if operation == '*':
  print("\n{}".format(a*b))

if operation == '/':
  print("\n{}".format(a-b))
