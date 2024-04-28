num=int(input())
lst=[0]*(num+1)
lst[1]=1
for i in range(2,num+1):
    lst[i]=lst[i-1]+lst[i-2]
print(lst[num])