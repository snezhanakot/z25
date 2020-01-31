items = []

_sum = 0
_mul = 1

while True:
    # while number := input('> '):
    # https://www.geeksforgeeks.org/walrus-operator-in-python-3-8/
    number = input('> ')
    if not number:
        break
    number = float(number)
    items.append(number)
    _sum += number
    _mul *= number

print(items)
print(_sum, _mul)
