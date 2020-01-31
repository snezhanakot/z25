items = []

sum_positive_numbers = 0
count_numbers = 0
while True:
    number = input('> ')
    if not number:
        break
    number = float(number)
    items.append(number)
    if number > 0:
        sum_positive_numbers += number
        count_numbers += 1

if count_numbers:
    print(sum_positive_numbers / count_numbers)
else:
    print('ZERO')
