# 嵌套调用
def test1():
    print('进入 test1 函数')             #|               |
    test2()                             #|               |
    print('退出 test1 函数')             #| test2— 待执行2  |
                                        #| test1- 待执行1 |
                                        #|_______________|
def test2():
    print('进入 test2 函数')             #待执行“收集器”  栈结构（先进后出）
    test3()
    print('退出 test2 函数')


def test3():
    print('进入 test3 函数')
    print('***正在执行 test3 函数***')
    print('退出 test3 函数')


test1()


# 函数嵌套调用测试
# **python不会直接执行定义函数中的代码，而是碰到调用函数时再去执行!**
def speak(msg):
    print('************')
    print(msg)
    print('************')


def greet(name, msg):
    print(f'My name is {name}, here is what I want to say next:')
    speak(msg)
    print('That\'s all.')


greet('Alex', 'Besides,')


# 互换位置也ok
def greet(name, msg):
    print(f'My name is {name}, here is what I want to say next:')
    speak(msg)
    print('That\'s all.')


def speak(msg):
    print('************')
    print(msg)
    print('************')


greet('Alex', 'Besides,')
