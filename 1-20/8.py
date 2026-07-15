# and用于判断其两侧的值是否都为True
print(True and True)
print(False and False)
print(False and True)
print(True and False)
print(7 > 8 and 8 > 7)

# and具备逻辑短路的能力
print(False and 3 / 0)  # 左边已经是False，不看右边直接得出结论
# print(True and 3/0)   报错 因为3/0
print(3 > 9 and 3 / 0)

# and返回的不一定是布尔值，它返回的是某个参与计算的值本身
# 规则：and会先看左边，如果左边是“假”，就直接返回左边，否则返回右边
# 备注：若参与and运算的值不是布尔值，那Python会自动转换为布尔值，然后再进行逻辑操作
print(2 - 2 and True)
print('' and True)
print(True and 8 / 2)
print(3 + 3 and 3 * 4)

# or用于判断其两侧，是否至少有一个为True（只要有一个是True，那就返回True）
# or返回的不一定是布尔值，它返回的是某个参与计算的值本身
# 规则：or会先看左边，如果左边是“真”，就直接返回左边，否则返回右边
# 备注：若参与or运算的值不是布尔值，那Python会自动转换为布尔值，然后再进行逻辑操作
print(True or 1 - 1)
print('5' or '2')
print(1 - 1 or 3 - 2)
print('你好' or '呀呀')
print(True or 3 / 0)  # or同样具备逻辑短路的能力
# print(False or 3/0)  报错

# not用于取反
# 备注：若参与not运算的值不是布尔值，那Python会自动转换为布尔值，然后再进行逻辑操作
print(not True)
print(not 'abc')
print(not 2 > 3)

#not返回的值一定是布尔值！
print(not(1-1))
