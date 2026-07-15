#新增
#方式一：通过列表的append方法，在列表尾部追加一个元素
list1=[10,20,30,40]
list1.append(50)
print(list1)
#方式二：通过列表的insert方法，在列表的指定下方处添加一个元素
list2=[10,20,40,50]
list2.insert(2,30)
print(list2)
#方式三：通过列表的extend方法，将可迭代对象中的内容依次取出，追加到列表尾部
list3=[10,20,30,40]
list3.extend('HAPPY')
list3.extend(range(1,4))
list3.extend([50,60,70])
print(list3)

#删除
#方法一：通过列表的pop方法，删除指定位置的元素，并将删除的元素返回
nums1=[10,20,10,30,40]
result=nums1.pop(2)
print(result)
print(nums1)
#方法二：通过列表的remove方法：删除列表中第一次出现的指定值
nums2=[10,20,10,30,40,50]
nums2.remove(10)
print(nums2)
#方法三：通过列表的clear方法，删除列表中的所有元素，变成空列表
nums3=[10,20,30,40]
nums3.clear()
print(nums3)
#通过del关键字，删除指定元素
nums4=[10,20,10,30,40,50]
del nums4[2]
print(nums4)

#修改
list5=[10,25,30,40]
list5[1]=20
print(list5)

#查询
list6=[10,20,30,40]
print(list6[3])