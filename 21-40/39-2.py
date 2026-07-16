key = 'love'
print('Guess the word!\n')
print('____')
list1 = ['l', 'o', 'v', 'e']
list2 = []
times = 1
while times <= 5:
    first = input('Guess the first letter is: ')
    if ord(first) == ord(list1[0]):
        print('Good!')
        print('l___')
        times = 1
        while times <= 5:
            second = input('Guess the second letter is: ')
            if ord(second) == ord(list1[1]):
                print('Good!')
                print('lo__')
                times = 1
                while times <= 5:
                    third = input('Guess the third letter is: ')
                    if ord(third) == ord(list1[2]):
                        print('Good!')
                        print('lov_')
                        times = 1
                        while times <= 5:
                            fourth = input('Guess the fourth letter is: ')
                            if ord(fourth) == ord(list1[3]):
                                print('Good!')
                                print('love')
                                print('Game succeeded!')
                                times += 10
                            elif ord(fourth) != ord(list1[3]):
                                if times < 5:
                                    print('Try again!')
                                times += 1
                    elif ord(third) != ord(list1[2]):
                        print('Try again!')
                        times += 1
            elif ord(second) != ord(list1[1]):
                print('Try again!')
                times += 1
    elif ord(first) != ord(list1[0]):
        print('Try again!')
        times += 1
if 5 < times < 10:
    print('Game failed!')
