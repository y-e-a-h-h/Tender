# python不会直接执行定义函数中的代码，而是碰到调用函数时再去执行

def add(m, n):
    print(f'{m}+{n}={m + n}')
    answer = m + n
    return answer  # return 会结束函数的运行
    # return后面不写东西返回None


result1 = add(100, 200)
print(result1)  # 不写return返回值就是None

# print函数是没有返回值的
res = print('Hello.')
print(res)
