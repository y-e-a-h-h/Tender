n = int(input('n= '))
list1 = []
for i in range(1, n + 1):
    enter = int(input(f'The {i} one: '))
    list1.append(enter)
print(list1)
first = list1[0]
maximum = first
for j in list1:
    if j >= maximum:
        maximum = j
print(f'Max: {maximum}')
small = list1[0]
minimum = small
for q in list1:
    if q <= small:
        minimum = q
print(f'Min: {minimum}')
