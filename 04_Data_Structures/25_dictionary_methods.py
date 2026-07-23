# keys方法：用于获取字典中所有的键
d1 = {'Wang': 86, 'Zhang': 95, 'Li': 75}
# keys方法：用于获取字典中所有的键
# keys方法的返回值不是list，而是一种叫做dict_keys的类型
result = d1.keys()
print(result)
print(type(result))
# dict_keys和列表类似，可以被遍历，但要注意的是：它不能通过下标访问元素
for i in result:
    print(i)

l1 = list(result)
print(l1)

# values方法：获取字典中所有的值
# 返回值类型是dict_values，特点与dict_keys一样
res = d1.values()
print(res)
print(type(res))

# items方法：获取字典中所有的键值对（每组键值对以元组的形式呈现）
# 返回值类型是dict_items，特点与dict_keys一样
res1 = d1.items()
print(type(res1))
print(res1)
