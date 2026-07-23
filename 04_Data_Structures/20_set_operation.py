# 集合A.difference(集合B)
# 集合的difference方法：找出集合A中不同于集合B的元素（集合A与集合B都不变）  返回值是一个新的集合
s1 = {10, 20, 30, 40}
s2 = {10, 40, 50}
result = s1.difference(s2)
res = s2.difference(s1)
print(result)
print(res)
print('#########################')

# 集合A.difference_update(集合B)
# 集合的difference.update方法：从集合A中，删除集合B中存在的元素（集合A会被修改，而集合B不会）无返回值
s1.difference_update(s2)
print(s1)
print('******************************')

# 集合A.union(集合B)
# 集合的union方法：合并两个集合，集合A和几何B都不变  返回值是一个新的集合
res1 = s1.union(s2)
res2 = s2.union(s1)
print(res1)
print(res2)
print('##########################')

# 集合A.issubset(集合B)
# 集合的issubset方法：判断集合A是否为集合B的子集   返回值是布尔值
s3 = {10, 20, 30, 40, 50}
s4 = {40, 50, 60}
result1 = s3.issubset(s4)
print(result1)
ss3 = {10, 20}
ss4 = set()
r = ss4.issubset(ss3)
print(r)
print('*********************')

# 集合A.issuperset(集合B)
# 集合的issuperset方法：判断集合A是否是集合B的超集    返回值是布尔值
r1 = s2.issuperset(s1)
print(r1)
r2 = ss3.issuperset(ss4)
print(r2)
print('######################')

# 集合A.isdisjoint(集合B)
# 判断集合A与集合B是否没有交集   返回值是布尔值
r3 = s3.isdisjoint(s2)
print(r3)
