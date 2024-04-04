list1=[]
listx=[]
listy=[]
for i in range(3):
    list1.append(list(map(int, input().split())))
for i in range(3):
    cnt0=0
    cnt1=0
    for j in range(3):
        if list1[i][0]==list1[j][0]:
            cnt0+=1
        if list1[i][1] == list1[j][1]:
            cnt1 += 1
    if cnt0==1:
        listx.append(list1[i][0])
    if cnt1==1:
        listy.append(list1[i][1])
print(listx[0],end=" ")
print(listy[0])
