n = int(input('n= '))
for i in range(1, n + 1, 2):
    print(i)

n = int(input('n= '))
for i in range(n, 0, -1):
    print(i)

n = int(input('n= '))
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)

n = int(input('n= '))
for i in range(1, n + 1):
    if i % 3 != 0:
        print(i)

n = int(input('n= '))
if n % 2 == 0:
    print('even number')
elif n % 2 != 0:
    print('odd number')

n = int(input('n= '))
while n != 0:
    print(n)
    n = int(input('n= '))

secret = '123456'
answer = input('Please enter your password: ')
while answer != secret:
    answer = input('Please enter your password: ')

t = 50
e = int(input('Guess: '))
while e != t:
    if e > t:
        print('Too high.')
    elif e < t:
        print('Too low.')
    e = int(input('Guess: '))
print('Yes!')
