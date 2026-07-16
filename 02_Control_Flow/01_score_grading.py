Name=input('Name: ')
Grade=input('Grade: ')
Class=input('Class: ')
Number=input('Number: ')
print(f'Ensure your information:{Name} from the {Grade} grade in class {Class},numbered {Number}')
Judge=input('True? ')
Score=input('Your score: ')
score=int(Score)
if score>=90:
    print('A')
elif score>=80:
    print('B')
elif score >=70:
    print('C')
elif score>=60:
    print('D')
else:
    print('E')
