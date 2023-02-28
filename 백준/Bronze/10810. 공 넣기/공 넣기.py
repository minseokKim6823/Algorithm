N,M=map(int,input().split())
list1=[0 for i in range(N)]
for i in range(M):
    s,e,num=map(int,input().split())
    for k in range(s-1,e):
            list1[k]=num
for i in range(len(list1)):
    print(list1[i],end=" ")
