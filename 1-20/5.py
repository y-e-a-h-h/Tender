# 单引号中打印单引号，用\'   双引号同理
print('i \'love\' you')

# 用\n换行
print('i\nlove\nyou')

# 用\\输出\
print('a\\b')

# 用\b删除前一个字符
print('你好呀\b')
print('helloo\b')

# 用\r使光标回到本行开头，覆盖输出
print('11\r22')

# 用\t表示水平制表符（让光标跳转到下一个制表位）
print('1234123412341234')
print('ab\tcd'.expandtabs(4))  # 使制表位的位数无论什么环境都为4位
print('abc\td')
print('abcd\ta')
print('你好\t爱你')
