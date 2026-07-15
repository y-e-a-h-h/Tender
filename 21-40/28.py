# python不会直接执行定义函数中的代码，而是碰到调用函数时再去执行

a, b = 100, 200  # 全局变量


def test():
    c, d = 'Hello!', 'Girls!'  # 局部变量
    global a  # 声明a是全局变量（可用于更改全局变量）
    a = 500
    print(a)
    print(b)
    print(c)
    print(d)


test()  # 调用
print('***************')
print(a)
print(b)

# 局部作用域 和 局部变量 ，会在函数调用时创建，在函数执行结束后销毁
print('@@@@@@@@@@@@')


def test2():
    m = 100
    m += 1
    print(m)


test2()
test2()

# 全局作用域和全局变量，会在程序开始时创建，在程序结束后销毁
print('$$$$$$$$$$$$$$$')
n = 100


def test3():
    global n
    n += 1
    print(n)
    return n


res = test3()
print(res)
test3()
test3()
print(n)
