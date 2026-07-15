key1 = 'l'
print('Welcome to the letter guessing challenge!')
print('You have 5 chances to guess in each level.\nEnter the letter \'q\' to exit the challenge.')
print('The first level: ')
i = 1
while i < 6:
    answer1 = input('Guess the first letter is  ')
    if answer1 == 'q':
        print('Challenge\'s finished.')
        i += 7
        break
    if answer1 == ' ':
        print('Please answer again.')
        continue
    if ord(key1) == ord(answer1):
        print('Congratulations! Let\'s move on to the next level!')
        break
    elif ord(key1) != ord(answer1):
        if ord(key1) > ord(answer1):
            print('That\'s too low!')
        elif ord(key1) < ord(answer1):
            print('That\'s too high!')
        i += 1
        if i == 6:
            continue
        print('Try again!')
if i == 6:
    print('Sorry! Challenge failed!')
elif i < 6:
    key2 = 'o'
    print('Welcome to the letter guessing challenge!')
    print('The second level: ')
    j = 1
    while j < 6:
        answer2 = input('Guess the first letter is  ')
        if answer2 == 'q':
            print('Challenge\'s finished.')
            j += 7
            break
        if answer2 == ' ':
            print('Please answer again.')
            continue
        if ord(key2) == ord(answer2):
            print('Congratulations! Let\'s move on to the next level!')
            break
        elif ord(key2) != ord(answer2):
            if ord(key2) > ord(answer2):
                print('That\'s too low!')
            elif ord(key2) < ord(answer2):
                print('That\'s too high!')
            j += 1
            if j == 6:
                continue
            print('Try again!')
    if j == 6:
        print('Sorry! Challenge failed!')
    elif j < 6:
        key3 = 'v'
        print('Welcome to the letter guessing challenge!')
        print('The third level: ')
        k = 1
        while k < 6:
            answer3 = input('Guess the first letter is  ')
            if answer3 == 'q':
                print('Challenge\'s finished.')
                k += 7
                break
            if answer3 == ' ':
                print('Please answer again.')
                continue
            if ord(key3) == ord(answer3):
                print('Congratulations! Let\'s move on to the next level!')
                break
            elif ord(key3) != ord(answer3):
                if ord(key3) > ord(answer3):
                    print('That\'s too low!')
                elif ord(key3) < ord(answer3):
                    print('That\'s too high!')
                k += 1
                if k == 6:
                    continue
                print('Try again!')
        if k == 6:
            print('Sorry! Challenge failed!')
        elif k < 6:
            key4 = 'e'
            print('Welcome to the letter guessing challenge!')
            print('The fourth level: ')
            l = 1
            while l < 6:
                answer4 = input('Guess the first letter is  ')
                if answer4 == 'q':
                    print('Challenge\'s finished.')
                    l += 7
                    break
                if answer4 == ' ':
                    print('Please answer again.')
                    continue
                if ord(key4) == ord(answer4):
                    print('Congratulations! Let\'s move on to the next level!')
                    break
                elif ord(key4) != ord(answer4):
                    if ord(key4) > ord(answer4):
                        print('That\'s too low!')
                    elif ord(key4) < ord(answer4):
                        print('That\'s too high!')
                    l += 1
                    if l == 6:
                        continue
                    print('Try again!')
            if l == 6:
                print('Sorry! Challenge failed!')
if i < 6 and j < 6 and k < 6 and l < 6:
    print('*****❤love❤*****')
    print('***❤I LOVE YOU❤***')
