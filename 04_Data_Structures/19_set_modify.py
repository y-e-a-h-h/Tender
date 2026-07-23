# 增
# add方法，无返回值，向集合中添加元素
from unittest import result

s1 = {10, 20, 30, 40, 50, 60}
s1.add(100)
print(s1)
# update方法，无返回值，向集合中批量添加元素(必须传递可迭代对象，例如：列表、元组、集合等）
s1.update((666, 777, 888, 999))
s1.update({'a', 'b', 'a'})
s1.update(range(2021, 2029))
print(s1)

# 删
# remove方法：从集合中移除指定元素（若元素不存在，会报错）  无返回值
s1.remove('a')
s1.remove(777)
print(s1)
# discard方法：从集合中移除指定元素（若元素不存在，不会报错）  无返回值
s1.discard(999)
s1.discard(100000)
print(s1)
# pop方法：从集合中移除一个任意元素   返回值是被溢出的那个元素
result = s1.pop()
print(s1)
print(result)
# clear方法：清空集合  无返回值
# s1.clear()
# print(s1)

# 改
# 用remove+add的组合，来达到“修改”的效果
s1.remove('b')
s1.add('hello')
print(s1)

# 查
# 用成员运算符
res = 20 in s1
print(res)
res1 = 50 not in s1
print(res1)
