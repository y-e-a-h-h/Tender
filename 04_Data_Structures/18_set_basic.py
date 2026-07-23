# 集合的特点：内部的元素无序（不保证顺序）、不能通过下标访问元素、会自动去除重复元素
# 定义有内容的【可变集合】
s1 = {10, 20, 30, 30, 40, 50, 60, 70, 70, 80, 90, 100}
s2 = {'hello', 'windy', 'happy', '健康', 'windy'}
s3 = {10, 1, 'hello', 'happy', 1, True, False, None}
s2.add('good')
print(type(s1), s1)
print(s2)
print(s3)
# 定义有内容的【不可变集合】
ss1 = frozenset({10, 20, 30, 40, 50, 60, 70, 80, 90})
ss2 = frozenset({'hello', 'windy', 'happy', '健康', 'windy'})
ss3 = frozenset({10, 1, 'hello', 'happy', 1, True, False, None})
print(type(ss1), ss1)
print(ss2)
print(ss3)

# frozenset接收的参数，可以是任意可迭代对象，但最终返回的一定是不可变集合
sss1 = frozenset([10, 20, 30, 40, 50, 60])
sss2 = frozenset({10, 20, 30, 'hello'})
sss3 = frozenset(('hello', 'good'))
print(sss1)
print(sss2)
print(sss3)

# 定义空集合（可变集合）
s4 = set()
print(type(s4), s4)
# 不能直接写{}来定义空集合，因为直接写{}定义的是：空字典
s5 = {}
print(type(s5))
# 定义空集合（不可变集合）
s6 = frozenset()
print(type(s6), s6)

# 集合中不能嵌套【可变集合】，但可以嵌套【不可变集合】
# 只有“不可变”的东西，才能安全的放进集合里
s101 = {10, 20, 30, 40, 50}
s202 = frozenset({100, 200, 300, 400})
l1 = ['a', 'b', 'c', 'd', 'e', 'f']
t1 = (9999, 8888, 7777, 6666)
s303 = {1111, 2222, 3333, s202}
print(s303)
