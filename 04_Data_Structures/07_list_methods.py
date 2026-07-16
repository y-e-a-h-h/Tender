# 使用index方法，查找指定元素在列表中第一次出现的下标，返回值是元素下标
fruits = ['banana', 'apple', 'watermelon', 'grape', 'orange']
result1 = fruits.index('apple')  # 嵌套列表不行
print(result1)
# 使用count方法，统计某个元素在列表中出现的次数，返回值是元素出现的次数
list1 = [10, 20, 30, 20, 10, 50, 10]
result2 = list1.count(10)  # 不统计嵌套列表中的元素
print(result2)
# 使用reverse方法，对列表进行反转（会改变原列表）
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2.reverse()
print(list2)
# 使用sort方法，对列表排序（默认从小到大），若想从大到小，可以将reverse参数设为True
# 嵌套列表不行
# 列表中都是数字
list3 = [4, 6, 1, 5, 2, 9, 3, 8, 0, 7]
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)
# 列表中的元素既有字符串又有数字 错误！！！
# 列表中的元素都是字符串，则按照字符串的Unicode编码大小进行排序
list4 = ['hello', 'hi', '你好', '333']
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)
