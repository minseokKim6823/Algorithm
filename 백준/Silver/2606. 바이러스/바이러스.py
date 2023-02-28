list1=[]
list2=[1]
a=int(input())
s=int(input())
t=0
cnt=-1
cnt1=0
for i in range(s):
    list1.append([int(k) for k in input().split()])
while(cnt<len(list2)):
    t=list2[cnt]
    for i in range(len(list1)):
        if(list1[i][0]==t):
            if list1[i][1] not in list2:
                list2.append(list1[i][1])
        elif(list1[i][1]==t):
            if list1[i][0] not in list2:
                list2.append(list1[i][0])
    cnt+=1
print(len(list2)-1)
