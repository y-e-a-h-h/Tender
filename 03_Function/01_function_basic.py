# 定义函数
def welcome():
    print('Hello!')
    print('Girl.')


# 调用函数
welcome()


def order(num, dish):
    print(f'You have ordered {num} {dish}s.')
    print(f'We hope the {dish} can bring you a good mood!\n')


order(2, 'chicken soup')
order(3, 'ice cream')
order(3, dish='cabbage')  # 3是位置参数，后者是关键字参数


def greet(name, gender, age, hobby):
    print(f'Hello everyone! My name is {name}, I am {age} years old, I am a {gender}, I like {hobby} in daily life.')
    print('I hope that we can have a good time during school!')


greet('Lily', 'female', 18, 'singing')
