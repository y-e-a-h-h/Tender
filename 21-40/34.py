Exercise_name = input('Exercise_name= ')
Days_of_exercise = int(input('Days_of_exercise= '))
Daily_goal = float(input('Your daily goal: '))
print(f'【{Exercise_name}】【{Days_of_exercise}days】Challenge (Please enter the daily quantity)')
total = 0
for i in range(1, Days_of_exercise + 1):
    numbers = int(input(f'The {i} day: '))
    total += numbers


def ave(total):
    answer = total / Days_of_exercise
    return answer


average = ave(total)
print(f'\n【{Exercise_name}】【{Days_of_exercise}days】 Exercise sum up\ntotal: {total}, average: {average}\n')

if average >= Daily_goal:
    print('Congratulations! Challenge succeeded!')
else:
    print('Sorry! Challenge failed! Keep going!')
