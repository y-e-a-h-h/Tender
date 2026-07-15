n=int(input('n= '))
list1=[]
for i in range(1,n+1):
    numbers=float(input(f'The {i} one: '))
    list1.append(numbers)
print(list1)
for j in range(0,n):
    if j<=n/2:
        temp=list1[j]
        list1[j]=list1[n-j-1]
        list1[n-j-1]=temp
    else:
        break
print(list1)


