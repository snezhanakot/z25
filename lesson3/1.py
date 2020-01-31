try:
    minimum = float(input('Minimum: '))
    maximum = float(input('Maximum: '))
    step = float(input('Step: '))
except ValueError:
    print('Ошибка')
else:
    while minimum <= maximum:
        result = -1.24 * minimum ** 2 + minimum
        print('x=', minimum, 'y=', result)
        minimum += step
