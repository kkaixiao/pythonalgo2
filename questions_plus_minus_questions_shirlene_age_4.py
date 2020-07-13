
# designed for Shirlene in 2020
import random

nPlus = 8

while nPlus > 0:
    num1 = random.randint(0, 20)

    num2 = random.randint(0, 20)

    if num1 + num2 <= 20:
        print(str(num1) + '  +  ' + str(num2) + ' =')
        nPlus -= 1

nMinus = 4

while nMinus > 0:
    num1 = random.randint(0, 20)

    num2 = random.randint(0, 20)
    if num1 - num2 >= 0:
        print(str(num1) + '  -  ' + str(num2) + ' =')
        nMinus -= 1