for n in range(1, 101):
    if n % 7 == 0 or n % 10 == 7 or n // 10 == 7:
        print('❌')
    else:
        print(n)
