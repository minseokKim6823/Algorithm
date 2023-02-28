s=int(input())
list1=[]
list2=[]
list3=[]
maxh=0
maxw=0
for i in range(6):
    list2=[int(i)for i in input().split()]
    list1.append(list2)
#print(list1)
for i in range(6):
    if(list1[i][0]==4 or list1[i][0]==3):
        if(list1[i][1]>maxh):
            maxh=list1[i][1]
for i in range(6):
    if(list1[i][0]==1 or list1[i][0]==2):
        if(list1[i][1]>maxw):
            maxw=list1[i][1]
#print(maxw,maxh)
for i in range(6):
    list1.append(list1[i])
#print(list1)
for i in range(10):
    if(list1[i][0]==list1[i+2][0]):
        a=list1[i+1][1]
        list3.append(a)
size1=maxw*maxh
size2=list3[0]*list3[1]
size=size1-size2
print(size*s)