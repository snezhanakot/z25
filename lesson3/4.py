items = []

max_element = None
while True:
    number = input('> ')
    if not number:
        break
    number = float(number)
    items.append(number)

    if not max_element or number >= max_element:
        max_element = number

print(items)
print('MAX', max_element)
