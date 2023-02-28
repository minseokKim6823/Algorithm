avg=0
result=0
list1=[]
for i in range(5):
    su=int(input())
    avg+=su
    list1.append(su)
list1.sort()
print(int(avg/5))
print(list1[2])