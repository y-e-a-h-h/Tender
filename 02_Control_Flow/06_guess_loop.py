q = 'Who loves me?'
a = 'Me'
g = ''
print(f'{q}')
g = input('❤')
while g != a:
    print(f'Again:{q}')
    g = input('❤')
    if g == a:
        print('I love you too ! ❤😘')
    else:
        print('😭')
