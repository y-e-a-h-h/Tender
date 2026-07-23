# 字典不能使用while循环遍历，但可以使用for循环遍历
d1 = {'Wang': 86, 'Zhang': 95, 'Li': 75}
for i in d1:
    print(i)
# key是每组键值对的唯一标识
for key in d1:
    print(f'{key}\'s score is {d1[key]}')

for key in d1.keys():
    print(f'{key}\'s score is {d1[key]}')

# 字典是一种以“键”找“值”的映射型容器
# 当需要唯一标识——对应信息的结构时，首选字典
