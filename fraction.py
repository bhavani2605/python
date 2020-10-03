from fractions import Fraction


def add_fractions(x, y):
    print('Sum of fractions: {0}'.format(x+y))


def calculate():
    x = Fraction(input('Enter your first fraction: '))
    y = Fraction(input('Enter your second fraction: '))
    add_fractions(x, y)
    again()


def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()