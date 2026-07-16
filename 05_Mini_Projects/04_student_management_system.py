names = []
scores = []
print('1. Add Student\n2. Delete Student\n3. Edit Student\n4. View All Students\n5. Exit')
while True:
    n = int(input('Please enter number: '))
    if n == 1:
        enter_name_to_add = input('Name: ')
        enter_score = float(input('Score: '))
        names.append(enter_name_to_add)
        scores.append(enter_score)
    if n == 3:
        enter_name_to_edit_score = input('Name: ')
        position = names.index(enter_name_to_edit_score)
        enter_score_to_edit = float(input('Edit to: '))
        scores[position] = enter_score_to_edit
    if n == 2:
        enter_name_to_delete = input('Name: ')
        position = names.index(enter_name_to_delete)
        names.pop(position)
        scores.pop(position)
    if n == 4:
        print(names)
        print(scores)
    if n == 5:
        break
