a = float(input('a= '))
b = float(input('b= '))


def add(a, b):
    print(f'{a}+{b}={a + b}')
    answer1 = a + b
    return answer1


result = add(a, b)
print(result)

print('*****************')

x = float(input('x= '))


def square(x):
    print(f'{x}*{x}={x * x}')
    answer2 = x * x
    return answer2


square(x)

print('@@@@@@@@@@@@@@@')


def calculate(a, b):
    answer3 = square(add(a, b))
    return answer3


result = calculate(a, b)
print(result)
