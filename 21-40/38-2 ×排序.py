sorted_list=[]
print('Enter 5 numbers.')
for i in range(1,6):
    enter_number=float(input(f'The {i} one: '))
    if i==1:
        sorted_list.append(enter_number)
        first=enter_number
    elif i>=2:
        if enter_number>=first:
            sorted_list.insert(int(f'{i}'),enter_number)
        else:
            sorted_list.insert(int(f'{i-1}'),enter_number)
print(sorted_list)