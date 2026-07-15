print('Category A Interview Inquiry')
name = input('Name: ')
a = float(input('Chinese: '))
b = float(input('Maths: '))
c = float(input('Foreign language: '))
if a + b + c >= 900 * 0.9 and a >= 225 and b >= 360 and c >= 225:
    print('You have successfully secured an interview!')
    print('Below are the time and location of the interview:')
    if a >= 245 and b >= 395 and c >= 245:
        print('Time: 1:00p.m. on May 17')
        print('Venue: Room A-A701, J Campus, W School')
    elif a >= 240 and b >= 390 and c >= 240:
        print('Time: 1:00p.m. on May 17')
        print('Venue: Room A-A702, J Campus, W School')
    elif a + b + c >= 866:
        print('Time: 1:00p.m. on May 16')
        print('Venue: Room A-A601, J Campus, W School')
    elif a + b + c >= 861:
        print('Time: 1:00p.m. on May 16')
        print('Venue: Room A-A701, J Campus, W School')
    elif a + b + c >= 858:
        print('Time: 8:00a.m. on May 15')
        print('Venue: Room A-A703, J Campus, W School')
    elif a + b + c >= 855:
        print('Time: 1:00p.m. on May 15')
        print('Venue: Room A-A704, J Campus, W School')
    else:
        print('Time: 1:00p.m. on May 13')
        print('Venue: Room A-A401, J Campus, W School')
else:
    print('We regret to inform you that you have not been selected for the Cateloge A Interview!')
