#自己定义的布尔值
a = True
b = False
print(type(a), a)
print(type(b))

#靠程序执行得到的布尔值
c = 5 > 7
d = 1 == 1
print(type(c),c)

#布尔类型是int类型的子类型，底层的本质是用1表示True，用0表示False
print(int(True))
print(int(False))

print(int(4+True))
print(float(5-False))
print(str(9*True))

print(7>True)
print(5<False)

#使用bool()将指定内容转换为布尔类型
print(bool(1))
print(bool(5))  #python中除0以外任何数转为布尔值后均为True
print(bool(0))
print(bool('hello'))   #python中除空字符串以外的任何字符串，转为布尔值都是True
print(bool(''))    #空格字符也是内容