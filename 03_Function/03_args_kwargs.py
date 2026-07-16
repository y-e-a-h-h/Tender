# 定义函数（使用*args去接收：可变位置参数）
def test1(*args):
    # 此处args的值是 元组 数据类型
    print(args)


# 调用函数
test1('A', 'abc', 123, 9)  # 只有位置参数可以交给args，关键字参数不可以！


# 定义函数（使用**kwargs去接收：可变关键字参数）
def test2(**kwargs):
    # 此处kwargs的值是 字典 数据类型
    print(kwargs)


# 调用函数
test2(A='Zhang', B='Wang', C='Lily')


# 定义函数（同时使用：可变位置参数、可变关键字参数）
def test3(a, b, *args, c='love', **kwargs):
    print('@@@@@@@@@@@@@@@@@')
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


# 调用函数
test3('A', 'abc', 888, 9, c='beloved', A='Zhang', B='Wang', C='Lily')
test3('A', 'abc', 888, 9, A='Zhang', B='Wang', C='Lily')
