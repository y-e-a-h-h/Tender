n = int(input('n= '))
if n == 2:
    print('Yes.')
for i in range(2, n):
    if n % i == 0:
        print('No.')
        break
    elif n % i != 0:
        i += 1
        if i >= n:
            print('Yes.')
