cnt=int(input())
S=0
list3=[]
list1=[[0 for i in range(100)] for k in range(100)]
for i in range(cnt):
    list2=[int(i) for i in input().split()]
    list3.append(list2)
for i in range(len(list3)):
    x = list3[i][0]
    y = list3[i][1]
    for j in range(10):
        for k in range(10):
            if list1[x+k][y+j]==0:
                list1[x+k][y+j]=1
            else:
                pass
            if list1[x+j][y+k]==0:
                list1[x+j][y+k]=1
            else:
                pass
for i in range(100):
    for k in range(100):
        if list1[i][k]==1:
            S+=1
print(S)