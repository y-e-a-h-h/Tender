# 递归调用
# 先打印后递归
n = int(input('n= '))


def welcome(n):
    print(f'Hello {n}')
    if n > 1:
        welcome(n - 1)


welcome(n)

# 先递归后打印
m = int(input('m= '))


def welcome1(m):
    if m > 1:
        welcome1(m - 1)  # !!待执行收集器（栈结构）!!
    print(f'Hello! {m}')


welcome1(m)
