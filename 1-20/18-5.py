for i in range(2, 102, 2):
    print(i)

for m in range(1, 101):
    if m % 2 == 0:
        print(m)

n = int(input('n= '))
a = 0
for i in range(1, n + 1):
    a += int(i)
print(a)
