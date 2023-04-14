num=int(input())
cnt=0
list2=[int(i) for i in input().split()]
list3=[]
b=max(list2)
a=min(list2)
list1=[True]*(b+1)
for i in range(2, int(b**0.5)+1):
    if(list1[i]==True):
        for j in range(i*2,b+1,i):
            list1[j]=False
for i in range(a,len(list1)):
    if list1[i]==True and i!=1:
        list3.append(i)
for i in range(len(list3)):
    if list3[i] in list2:
        cnt+=1
print(cnt)