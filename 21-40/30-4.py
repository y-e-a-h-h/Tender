temp = int(input('temp= '))
unit = input('unit= ')


def convert_temp(temp, unit):
    if unit == 'C':
        print(f'{temp * 9 / 5 + 32}')
    elif unit == 'F':
        print(f'{(temp - 32) * 5 / 9}')


convert_temp(temp, unit)
