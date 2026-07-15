a = 100
b = 100
print(a == b)

a = 100
b = 100
print(a != b)

a = 10
b = 100
print(a >= b)

# 用==来判断两边是否相等
x = 1
y = '1'
result = x == y
print(result)

# 用!=来判断两边是否不相等
m = 2
n = '2'
res = m != n
print(res)

h = '555'
i = '555'
print(h == i)

u = 'abc'
v = 'xyz'
print(u < v)  #比较Unicode编码，从第一位开始，第一位比较出结果则不看后面的直接得出结论

e = '爱你'
f = '我爱你'
print(e < f)

q = 'abcd'
p = 'abcdef'
print(p < q)  #因为abcd的Unicode都一样，所以比较长度

# 使用ord()查看指定字符的Unicode编码
print(ord('a'))
print(ord('我'))

# 使用chr()将Unicode编码转为字符
print(chr(66))
