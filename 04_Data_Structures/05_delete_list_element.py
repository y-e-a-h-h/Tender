total_nums = int(input('n= '))
list1 = []
for i in range(1, total_nums + 1):
    enter = int(input(f'The {i} one: '))
    list1.append(enter)
print(list1)
enter_for_delete = int(input('Please enter a number: '))
list2 = []
for j in list1:
    if j != enter_for_delete:
        list2.append(j)
print(list2)
