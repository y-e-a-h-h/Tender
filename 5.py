#定义函数时，使用*args(变量不一定非要用args,比如写*data也可以),将收到的多个参数，打包成一个元组
def test(*args):  # 可变参数（*args）无论传入多少个参数都可以接受
    print(f'I\'m the test function, and the argument passed to me is: {args}', f'{type(args)}')


list1 = [100, 200, 300, 400]
tuple1 = ('hello', 'good', 'wonderful')

# 函数调用时，正常传递：列表 或 元组
test(list1)
test(tuple1)

# 函数调用时，使用*对：列表 或者 元组进行解包后，再传递参数
test(*list1)  # 此种写法相当于test(100,200,300)
test(*tuple1)
