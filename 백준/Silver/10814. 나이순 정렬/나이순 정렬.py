lst1=[]
lst3=[]
su=int(input())
for i in range(su):
    lst2=[str(i) for i in input().split()]
    lst2[0]=int(lst2[0])
    lst2.append(lst2[0]*100000+i)
    lst1.append(lst2)
lst1=sorted(lst1)
for i in range(len(lst1)):
    for j in range(2):
        lst1[i].append(lst1[i][0])
        del lst1[i][0]
lst1=sorted(lst1)
for i in range(len(lst1)):
    print(lst1[i][1],lst1[i][2])