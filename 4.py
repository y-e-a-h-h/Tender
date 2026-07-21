# 元组的index方法：获取指定元素在元组中第一次出现的下标
t1 = (0, 10, 20, 30, 40, 50, 60)
res1 = t1.index(30)
print(res1)
# 元组的count方法：统计指定元素在元组中出现的次数
t2 = (10, 30, 20, 40, 20, 20)
res2 = t2.count(20)
print(res2)


# 函数的可变参数*args就是一个元组
def demo(*args):
    return sum(args)


result = demo(100, 200, 300)
print(result)

# 元组的while循环遍历
tt = (0, 10, 20, 30, 40, 50, 60)
index = 0
while index < len(tt):
    print(tt[index])
    index += 1

# 元组的for循环遍历
tt = (0, 10, 20, 30, 40, 50, 60)
for i in tt:
    print(i)
