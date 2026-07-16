n = int(input('n= '))
for i in range(1, n + 1):
    print(f'{i}')
    if i == 2:
        continue
    print('A')
    for j in range(1, n + 1):
        print('B')
        if j == 3:
            break
        print('C')
    print('D')
