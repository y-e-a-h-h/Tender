# 序列的相加
list1 = [10, 20, 30, 40]
list2 = [50, 60, 70, 80]
list3 = list1 + list2
print(list3)
tuple1 = (10, 20, 30, 40)
tuple2 = (50, 60, 70, 80)
tuple3 = tuple1 + tuple2
print(tuple3)
str1 = 'hello'
str2 = 'princess'
str3 = str1 + str2
print(str3)

# 序列的相乘（相加）
# n是整数不能是浮点数，不会更改原来的序列
n = int(input('n= '))
res1 = list1 * n
print(res1)
res2 = tuple1 * n
print(res2)
res3 = str1 * n
print(res3)
