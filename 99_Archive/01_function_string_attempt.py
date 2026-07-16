name = input('name= ')
text = input('text= ')


def greet(name):
    return f'Hello! {name}'


def shout(text):
    return f'{text}!!!'


def announce(name):
    answer = greet(f'{name}' + '! ' + shout(f'{text}'))
    return answer


result = announce(name)
print(result)
