#对列表进行切片（元组字符串一样）（字符串空格也算有效元素）
list1=[10,20,30,40,50,60,70,80,90,100]
list2=list1[0:5:1]
print(list2)
list3=list1[2:9:2]
print(list3)
list4=list1[::]
print(list4)
list5=list1[4:99999:]
print(list5)

#当起始索引大于结束索引时，步长必须为负数，否则结果是空列表
list6=list1[20:2:-1]
print(list6)
list7=list1[20:0:1]
print(list7)

#当同时省略起始索引和结束索引时，如果步长为负数，那python会自动对调起始位置和结束位置
list8=list1[::-2]
print(list8)