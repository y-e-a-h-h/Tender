n = int(input('n= '))
a = ''
b = ''
for i in range(1, n + 1):
    a += str(i)
for j in range(n - 1, 0, -1):
    b += str(j)
print(a + b)

n = int(input('n= '))
for i in range(1, n + 1):
    e = ''
    for k in range(1, i + 1):
        e += str(k)
    f = ' ' * (n - i)
    y = f + e
    print(y)

n = int(input('n= '))
for i in range(1, n + 1):
    line = ''
    for k in range(1, i + 1):
        line += str(k)
    for j in range(i - 1, 0, -1):
        line += str(j)
    line = ' ' * (n - i) + line + ' ' * (n - i)
    print(line)
