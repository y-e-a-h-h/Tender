n = int(input('How many numbers you want to enter: '))
for i in range(1, n + 1):
    b = int(input(f'Number{i}: '))
    if i==1:
        m=b
    elif b > m:
        m = b
print(m)
