operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(num1, num2))
    print(num1 + num2)

elif operation == '-':
    print('{} - {} = '.format(num1, num2))
    print(num1 - num2)

elif operation == '*':
    print('{} * {} = '.format(num1, num2))
    print(num1 * num2)

elif operation == '/':
    print('{} / {} = '.format(num1, num2))
    print(num1 / num2)

else:
    print('You have not typed a valid operator, please run the program again.')