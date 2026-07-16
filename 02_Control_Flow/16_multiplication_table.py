n = int(input('n= '))
for m in range(1, n + 1):
    for q in range(1, n + 1):
        if m <= q:
            b = f'{m}*{q}=' + str(m * q)
            print(' ' + b, end='')
    print()
