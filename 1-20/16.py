a='我最喜欢'
b='的人是你'
print(a+b)
c='I love '
c+='you❤'
print(c)
#加密代码
text = input('Please enter the text to be encrypted: ')
secret = ''
for n in text:
    secret += chr(ord(n) + 1)
print(f'The encrypted text is: {secret}')
#解密代码
text=input('Please enter the code to be decrypted: ')
secret=''
for n in text:
    secret+=chr(ord(n)-1)
print(f'The decrypted text is: {secret}')