# None是一个特殊的字面量，它表示：空值/无值/无意义。
# None的类型是NoneType.
# None转为布尔值是False
# 不能参与数学运算，也不能参与字符串拼接。
msg = None
print(type(msg))
print(bool(msg))
if msg:
    print('Hello.')
if not msg:
    print('Good.')
