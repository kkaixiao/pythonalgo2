import random

nPlus = 8

while nPlus > 0:
    num1 = random.randint(0, 20)

    num2 = random.randint(0, 20)

    if num1 + num2 <= 20:
        print('{:2d}'.format(num1) + '  +  ' + '{:2d}'.format(num2) + '  =')
        nPlus -= 1

nMinus = 4

while nMinus > 0:
    num1 = random.randint(0, 20)

    num2 = random.randint(0, 20)
    if num1 - num2 >= 0:
        print('{:2d}'.format(num1) + '  -  ' + '{:2d}'.format(num2) + '  =')
        nMinus -= 1
