# 任何类型都可以转换为字符串类型
# type函数用来看类型

print(type(18))
print(type(66.6))

a = str(18)
b = str(66.6)
print(type(a), a)
print(type(b), b)

# 可转换为整型    int('7 9')不行 int('15.6')不行
c = int(15.6)
d = int('79')
e = int(' 66 ')
f = int(48)
print(f)

# 转换为浮点型   float('5. 7')不行
float(18)
float('15.6')
float('48')
float(18.6)
float(' 5.6 ')
