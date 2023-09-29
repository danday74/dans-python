def program1():

    print(f'\nRunning program 01_01')

    count = 3
    values = []

    for i in range(count):

        # TODO: Currently, an error occurs if the user does not enter an integer
        #       An enhancement would be to handle the error and ask again if the value entered is not an integer
        value = input('Please input a number: ')
        values.append(int(value))

    total = sum(values)
    avg = total / count

    print(f'The {count} numbers you typed in were {values}')
    print(f'The sum of the numbers is {total}')
    print(f'The average of the numbers is {avg}')  # TODO: Only display 1 decimal place


def program2():
    print(f'\nRunning program 01_02')

    name = input('Please input your name: ')
    print(f'Hello World. This program was written by {name} and it works perfectly.')


def program3():
    print(f'\nRunning program 01_03')


def program4():
    print(f'\nRunning program 01_04')


def program5():
    print(f'\nRunning program 01_05')


if __name__ == '__main__':

    program = input('Which program do you want to run (1-5)? ')

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
