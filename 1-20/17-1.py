secret = '123456'
text = ''
attempts = 0
while attempts < 3:
    text = input('Please enter your password: ')
    if text == secret:
        print('Welcome back!')
        break
    elif text != secret:
        attempts += 1
        if attempts < 3:
            print(
                f'Your password is incorrect!\nYou have tried for {attempts} times,and you only have {3 - attempts} times!')
        else:
            print('Your account has been locked.')
