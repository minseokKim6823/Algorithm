N,M = map(int,input().split())
list1 = [i+1 for i in range(N)]
for c in range(M):
    list2 = []
    i,j=map(int,input().split())
    for k in range(i-1,j):
        list2.append(list1[k])
    list2.reverse()
    for k in range(len(list2)):
        list1[i+k-1]=list2[k]
for i in range(len(list1)):
    print(list1[i],end=" ")