# 并集
s1 = {10, 20, 30, 40, 50, 60}
s2 = {40, 50, 60, 70, 80, 90}
result1 = s1 | s2
print(result1)

# 交集
result2 = s1 & s2
print(result2)

# 差集
result3 = s1 - s2  # 得到属于s1集合但不属于s2集合的元素
print(result3)
result4 = s2 - s1  # 得到属于s2集合但不属于s1集合的元素
print(result4)

# 对称差集
result5 = s1 ^ s2  # 属于s1集合或属于s2集合但又不同时属于s1集合和s2集合的元素
print(result5)
