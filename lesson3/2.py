size = int(input('Size? '))

for i in range(1, size + 1, 1):
    for j in range(1, size + 1, 1):
        print(i * j, end='\t')
    print()
