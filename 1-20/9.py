#0b开头表示二进制
num1=0b11001
#o开头表示八进制
num2=0o1034
#x开头表示十六进制
num3=0x1CF
#python中非十进制数字在进行计算打印等操作时会自动将其转换为十进制
print(num1,num2,num3)
print(num1+1)
print(str(num2))
print(num3>300)

#使用bin()将十进制转换为二进制字符串
a=10086
print(bin(a))
#使用oct()将十进制转换为八进制字符串
b=520
print(oct(b))
#使用hex()将十进制转换为十六进制字符串
c=886
print(hex(c))
print(type(bin(a)),type(oct(b)),type(hex(c)))  #bin(),oct(),hex()返回值的类型都是字符串

#使用int()将指定进制的数转化为十进制数字
x=int('0b1110010100',2)
y=int('0o1314520',8)
z=int('0x5566DB',16)
print(x,y,z)
print(type(x),type(y),type(z))