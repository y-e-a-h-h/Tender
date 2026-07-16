print('Please enter the scores of students.')
n=int(input('The amount of students is: '))
list1=[]
for i in range(1,n+1):
    enter=float(input(f'Student {i}: '))
    list1.append(enter)
print(list1)
first=list1[0]
maximum=first
small=list1[0]
minimum=first
for j in list1:
    if j>=maximum:
        maximum=j
    elif j<minimum:
        minimum=j
    else:
        continue
print(f'The highest score is {maximum} from Student  .\nThe lowest score is {minimum} from Student  ')
total=0
for q in list1:
    total+=q
print(f'The average score is {total/n}.')
number_of_passes=0
for k in list1:
    if k>=60:
        number_of_passes+=1
print(f'The number of people who passed the passing line is {number_of_passes}.')
list2=[]
while list1!=[]:
    list2.append(minimum)
    list1.remove(minimum)
    if list1!=[]:
        minimum=list1[0]
        for l in list1:
            if l<=minimum:
                minimum=l
            else:
                continue
    else:
        break
print(list2)








