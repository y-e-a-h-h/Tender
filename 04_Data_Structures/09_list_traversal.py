# 定义一个成绩列表
score_list = [67, 95, 62, 57, 58, 94, 98, 73]
# 使用while循环遍历列表
index = 0
while index < len(score_list):
    print(index)
    index += 1

index = 0
while index < len(score_list):
    print(score_list[index])
    index += 1

#for循环遍历
list1=[5,15,25,35,45,55,65,75,85,95]
#写法一
for item in list1:
    print(item)
#写法二（通过range函数和len函数按照索引遍历）
for index in range(len(list1)):
    print(list1[index])
#写法三（通过enumerate函数，同时获取下标（索引值）和元素）
#enumerate的start参数，可以让计数从指定值开始（改变的是循环时的编号，不是真正的索引值）
for index,item in enumerate(list1):
    print(index,item)
for index,item in enumerate(list1,start=1000):
    print(index,item,list1[0])
