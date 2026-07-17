nums=[10,20,30,40,50]
nums.append(60)
nums.insert(2,25)
nums.pop(nums.index(40))
nums[0]=5
print(nums)

letters=['a','b','c','d','e','f','g']
print(letters[0:3])
print(letters[2:5])
print(letters[-2:])
print(letters[::-1])

list1=[3,8,1,9,4,7,]
n=0
list2=[]
for i in list1:
    print(f'{i*i}')
    list2.append(i+1)
    if i%2==0:
        n+=1
print(n)
print(list2)

a=[1,2,3,4,5]
b=[4,5,6,7,8]
a.extend(b)
print(a)
c=[]
for i in a:
    if i not in c:
        c.append(i)
print(c)
