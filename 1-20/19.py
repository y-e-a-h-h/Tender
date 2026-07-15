# for循环
i = 1
for i in range(1, 31):
    print(f'The {i} day')
    for j in range(1, 4):
        print(f'This is the {j} group')
    print(f'Day {i} task completed! Keep it tomorrow!')
    print()
print(f'The {i} day plan is completed! Wonderful!')

# while循环
m = 1
while m <= 30:
    print(f'The {m} day')
    n = 1
    while n <= 3:
        print(f'This is the {n} group')
        n += 1
    print(f'Day {m} task completed! Keep it tomorrow!')
    m += 1
print(f'The {m - 1} day plan is completed! Wonderful!')
