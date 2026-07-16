#写法一
print('What\'s your name?')
Name=input()
print('How old are you?')   #输出
age=input()     #输入
print(f'{Name} is {age} years old.')
print(type(age))
print(f'And {Name}\'s sister is {int(age)+3}.')

#写法二
name=input('Your name: ')
num=input('How many times you have been to America? ')
print(f'{name} has been to America for {num} times.')

