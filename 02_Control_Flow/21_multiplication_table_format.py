n = int(input('n= '))
for i in range(1, n + 1):  # 行
    for j in range(1, i + 1):  # 每行需打印几个
        print(f'{j}*{i}=' + str(i * j) + ' ', end=' ')
    print()
