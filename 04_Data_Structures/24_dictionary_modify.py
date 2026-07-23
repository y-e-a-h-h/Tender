# 查询
d1 = {'Wang': 43, 'Chen': 98, 'Zhang': 76}
# 直接取值，若键key不存在，会报错
result = d1['Chen']
print(result)
# 安全取值，若键key不存在，则会返回默认值（若没有设置默认值，则会返回None）（第二个参数是默认值）
result1 = d1.get('Zhang', 'Sorry! The key does not exit!')
print(result1)

# 新增
d1['Sun'] = 77
print(d1)

# 修改
d1['Sun'] = 87
print(d1)
# 批量修改
d1.update({'Sun': 89, 'Wang': 57})
print(d1)

# 删除
# 删除指定key所对应的那组键值对
del d1['Wang']
print(d1)
# 删除指定key所对应的那组键值对,并返回这个key所对应的值
res = d1.pop('Chen')
print(d1)
print(res)
# pop方法可以设置默认值：当要删除的key不存在的情况下，程序不会报错，并返回这个默认值（第二个参数是默认值）
res1 = d1.pop('CC', 'Sorry! The key does not exit!')
print(res1)
print(d1)
# 清空字典
d1.clear()
print(d1)
