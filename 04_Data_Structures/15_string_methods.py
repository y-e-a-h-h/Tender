# 字符串的下标
msg = 'hello welcome to Zhejiang.'
print(msg[5])
print(msg[-1])
# 字符串中的字符不可修改
# 字符串不能嵌套
# 字符串的index方法：获取指定字符在字符串中第一次出现的下标
result = (msg.index('o'))
print(result)
# 字符串的split方法：将字符串按照指定字符进行分割，并返回一个列表
msg1 = 'hello@welcome@to@Hangzhou'
res = msg1.split('@')
print(res)
# 字符串的replace方法：将字符串中的某个字符片段，替换成目标字符串
res1 = msg.replace('h', 'H')
print(res1)
# 字符串的count方法：统计指定字符在字符串中出现的次数
res2 = msg.count('o')
print(res2)
# 字符串的strip方法：从某个字符串中删除指定字符串中的任意字符
# 规则：从字符串两端开始删除，直到遇到第一个不在指定字符串中的字符就停下
msg2 = '6666hel6l6o666'
result1 = msg2.strip('6')
print(result1)
msg3 = '1234aaa12aa34aa4321'
result2 = msg3.strip('1324')  # 只要有字符在（）中就会删
print(result2)

aa = '   啊   '
print(aa)
print(aa.strip())  # 默认删空格

print(len(msg))
# max() min() sorted() 也能用，但是一般不用

# 字符串的循环遍历
index = 0
while index < len(msg):
    print(msg[index])
    index += 1

for i in msg:
    print(i)
