# 限制函数传参
# /前只能用位置参数，*后只能用关键字参数
# /和*同时出现时，/只能出现在*前面
# 定义函数时，通过 形参名=值 的形式，为参数指定一个默认值
# 默认参数必须要放在必选参数的后面，某个形参一旦设置了默认值那它之后的所有形参也必须要写默认值!
def greet(name, /, gender, *, age, hobby, msg='I hope that we can have a good time during school!'):
    print(f'Hello everyone! My name is {name}, I am {age} years old, I am a {gender}, I like {hobby} in daily life.')
    print(f'{msg}')


greet('Lily', 'female', age=18, hobby='singing')
greet('Lily', 'female', age=18, hobby='singing', msg='hello')

print('Hello', end='!!!')
# print函数底层给end参数设置了默认值
