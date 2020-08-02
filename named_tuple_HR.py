"""
Print the average marks of the list corrected to 2 decimal places. marks is at any position in the table

namedtuple: >>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y


#User 1 code:
from collections import namedtuple
N = int(input());student = namedtuple('student',input().strip().split())
print(sum(float(student(*input().strip().split()).MARKS) for _ in range(N))/N)

#Uset 2 code:
N, headers, total = int(input()), list(input().split()), 0
for _ in range(N):
    total += int(list(input().split())[headers.index('MARKS')])
print(total/N)



"""

#my code
from collections import namedtuple
#def marks_index(cat):
    
n = int(input())
cat = list(input().strip().split())
for i in range(len(cat)):
    if cat[i] =='MARKS':
        break

student = []
for j in range(n):
    data = list(input().strip().split())
    student.append(int(data[i]))

sum1 = 0
for k in range(n):
    sum1 = sum1 + student[k]
print(sum1/n)
