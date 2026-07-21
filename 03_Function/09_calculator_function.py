# def step1():
#     print('step 1 has been done.')
#     step2()
#
#
# def step2():
#     print('step 2 has been done.')
#     step3()
#
#
# def step3():
#     print('step 3 has been done.')
#
#
# step1()

a = float(input('a= '))
b = float(input('b= '))
op = input('op= ')


def add(a, b):
    print(f'{a}+{b}={a + b}')
    answer1 = a + b
    return answer1


def multiply(a, b):
    print(f'{a}*{b}={a * b}')
    answer2 = a * b
    return answer2


def calc(op, a, b):
    if op == '+':
        answer3 = add(a, b)
        return (answer3)
    elif op == '*':
        answer4 = multiply(a, b)
        return answer4
    else:
        print('Unknown operations')
        return None


result=calc(op, a, b)
print(result)
