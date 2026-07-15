age = int(input('Please enter your age: '))
has_report = input('Have you submitted your medical examination report? (Yes/No)')
level = int(input('Please enter your member level(1/2/3): '))

if 18 <= age <= 45:
    if has_report=='Yes':
        if level==1:
            print(f'Dear valued {level} level member: Upon completion of the competition, you will receive a commemorative T-shirt!')
        elif level==2:
            print(f'Dear valued {level} level member:Upon completion of the competition, you will receive a pair of premium running shoes!')
        elif level==3:
            print(f'Dear valued {level} level member:Upon completion of the competition, you will receive a pair of sports earphones!')
        else:
            print('Your input is incorrect!')
    elif has_report=='No':
        print('Please submit your medical examination report first!')
    else:
        print('Your input is incorrect!')
else:
    print('We regret to inform you that your age does not meets the competition requirements!')

