# 使用内置的sorted函数，返回一个排序后的新容器（不改变原容器，默认顺序：从小到大）
# 都是数字
nums = [5, 3, 4, 8, 9, 6, 1, 0, 2, 7]
result = sorted(nums)
print(result)
result1 = sorted(nums, reverse=True)
print(result1)
# 既有数字又有字符串不行！！！
# 都是字符串：按Unicode编码排序
list1 = ['hello', '你好', 'big', '快乐']
result2 = sorted(list1)
print(result2)
# 使用内置的len函数，获取容器中元素的总数量，返回值是元素总数量
list2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
result3 = len(list2)
print(result3)
list3 = [1, 2, 3, 4, [5, 6, 7, 8, 9]]
result4 = len(list3)
print(result4)
# 使用内置的max函数，获取容器中的最大值，返回值是最大值
# 都是数字
nums1 = (4, 6, 2, 8, 5, 9, 3)
result5 = max(nums1)
print(result5)
# 既有数字又有字符串不行！！！
# 都是字符串：按Unicode编码比较
list4 = ['hello', '你好', 'big', '快乐']
result7 = max(list4)
print(result7)
# 使用内置的min函数，获取容器中的最小值，返回值是最小值
# 都是数字
nums2 = (4, 6, 2, 8, 5, 9, 3)
result11 = min(nums2)
print(result11)
# 既有数字又有字符串不行！！！
# 都是字符串：按Unicode编码比较
list11 = ['hello', '你好', 'big', '快乐']
result1111 = min(list11)
print(result1111)
# 使用内置的sum函数，对容器中的数据进行求和（元素只能是*数值*）(整型and浮点型）
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result0 = sum(numbers)
print(result0)
