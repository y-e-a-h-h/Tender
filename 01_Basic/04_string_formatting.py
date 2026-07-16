a = 'wang'
b = 'male'
c = '18'
d = '60'
info = 'my name is ' + a + ' , my gender is ' + b + ' , my age is ' + c + ' , my weight is ' + d
print(info)

a = 'wang'
b = 'male'
c = 18
d = 60
info2 = 'my name is %s,my gender is %s,my age is %i, my weight is %.2f' % (a, b, c, d)
print(info2)

info3 = f'my name is {a},my gender is {b},my age is {c},my weight is {d}'  # f表示f-string格式化字符串字面量
print(info3)
