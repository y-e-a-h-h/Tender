t1 = (0, 1, 2, 3, 4, 5, 6, 7)
t2 = ('hello', 'hi', 'happy')
t3 = (100, True, 'good', None)
t4 = (100, True, 'good', None, (1, 2, 3))
print(type(t1))
print(t1[3])
# 元组中的元素不可修改
# 元组中如果存放了可变类型（列表），那可变类型中的内容仍可修改
t5 = (0, 1, 2, 3, 4, [10, 20, 40, (1000, 2000, ['hello', 'great'])])
t5[5][2] = 30
t5[5][3][2][0] = 'hi'
print(t5)

# 定义空元组
t6 = ()
t7 = tuple()
# 定义只有一个元素的元组
t8 = (1,)
t9 = ('hello',)
tt = (
    'yes'
    'no'
)
print(type(tt), tt)
