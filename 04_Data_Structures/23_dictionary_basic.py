# 字典
# 对应关系：键(key)与值(value)的对应关系
# 定义有内容的字典
d1 = {'Wang': 15, 'Jing': 16, 'Ann': 19}
#       |     |
#      key   value
# 字典中的key不能重复，若出现重复，则后写的会覆盖之前写的

# 定义空字典
d2 = {}
d3 = dict()
print(type(d1), d1)

# 字典中的键key必须是不可变类型，但值value可以是任意类型
d1 = {'Wang': 15, 'Jing': 16, 'Ann': 19}
d11 = {250: 15, 'Jing': 16, 'Ann': 19}
d12 = {('Big', 'Strong'): 15, 'Jing': 16, 'Ann': 19}
print(d1)
print(d11)
print(d12)

# 字典可以嵌套
student_dict1 = {2026010507: {'Name': 'Jack', 'Age': 18, 'Score': 92},
                 2026010103: {'Name': 'Anna', 'Age': 18, 'Score': 94},
                 2026011311: {'Name': 'Jackson', 'Age': 18, 'Score': 99}}
student_dict2 = {
    2026010301: {
        'Name': 'Wang',
        'Age': 18,
        'Score': 92.5
    },
    2026011004: {
        'Name': 'Kate',
        'Age': 18,
        'Score': 84
    },
    2026011701: {
        'Name': 'Jason',
        'Age': 18,
        'Score': 97
    }
}
print(student_dict1)
print(student_dict2)
