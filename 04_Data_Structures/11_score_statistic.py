score = []
while True:
    scores = input('Please enter the score: ')
    if scores == 'finish':
        break
    else:
        score.append(float(scores))
print(score)
print(f'total count: {len(score)}')
print(f'The highest score is: {max(score)}')
print(f'The lowest score is: {min(score)}')
pass_count = 0
for i in score:
    if i >= 60:
        pass_count += 1
print(f'Pass Rate: {(pass_count / len(score)) * 100:.2f}%')
excellent_count = 0
for j in score:
    if j >= 90:
        excellent_count += 1
print(f'Excellent Rate: {(excellent_count / len(score)) * 100:.2f}%')
print(f'The average score is: {sum(score) / len(score):.2f}')
