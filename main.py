def program1():

    print(f'\nRunning program 01_01')

    count = 3
    values = []

    for i in range(count):

        # TODO: Currently, an error occurs if the user does not enter an integer
        #       An enhancement would be to handle the error and ask again if the value entered is not an integer
        value = input('\nPlease input a number: ')
        values.append(int(value))

    total = sum(values)
    avg = total / count

    print(f'\nThe {count} numbers you typed in were {values}')
    print(f'\nThe sum of the numbers is {total}')
    print(f'\nThe average of the numbers is {avg}')  # TODO: Only display 1 decimal place


def program2():
    print(f'\nRunning program 01_02')

    name = input('\nPlease input your name: ')
    print(f'\nHello World. This program was written by {name} and it works perfectly.')


def program3():
    print(f'\nRunning program 01_03')

    value1 = ''
    value1isinteger = False
    while not value1isinteger:
        value1 = input('\nPlease input your first integer: ')
        value1isinteger = value1.isdigit()

    value2 = ''
    value2isinteger = False
    while not value2isinteger:
        value2 = input('\nPlease input your second integer: ')
        value2isinteger = value2.isdigit()

    print(f'\nThe first number you input was: {value1}')
    print(f'\nThe second number you input was: {value2}')

    if value1 > value2:
        print(f'\nThe first number {value1} is greater than the second number {value2}')
    elif value1 < value2:
        print(f'\nThe first number {value1} is less than the second number {value2}')
    else:
        print(f'\nThe first number {value1} is equal to the second number {value2}')


def program4():
    print(f'\nRunning program 01_04')

    print(f'\nEvery integer from 0 to 9 inclusive')
    for i in range(10):
        print(f'\n{i}')

    print(f'\nEvery integer from 5 to 30 inclusive')
    for i in range(5, 31):
        print(f'\n{i}')

    print(f'\nEvery odd integer from 1 to 20 inclusive')
    for i in range(1, 21, 2):
        print(f'\n{i}')

    print(f'\nEvery integer from -100 to -80 inclusive')
    for i in range(-100, -79):
        print(f'\n{i}')


def program5():
    print(f'\nRunning program 01_05')


if __name__ == '__main__':

    program = input('\nWhich program do you want to run (1-5)? ')

    if program == '1':
        program1()
    elif program == '2':
        program2()
    elif program == '3':
        program3()
    elif program == '4':
        program4()
    elif program == '5':
        program5()
    else:
        print(f'\nUnrecognised program')
