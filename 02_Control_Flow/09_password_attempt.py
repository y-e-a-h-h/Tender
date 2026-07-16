secret = '123456'
enter = ''
ask = 'Please enter your password: '
text = input(f'{ask}')
n = 0
if text == secret:
    print('Welcome back!')
elif text != secret:
    while n < 2:
        if text == secret:
            print('Welcome back!')
            n += 3
        else:
            n += 1
            print(f'Your password is incorrect!\nYou have tried for {n} time.And you only have {3 - n} times!')
            text = input(f'{ask}')
            if n >= 2:
                print('Your account has been locked.')
