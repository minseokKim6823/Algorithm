T= int(input())

for i in range(T):
    lst = []
    K= int(input()) #층 1
    N= int(input()) #호 3
    for j in range(1, N+1):
        lst.append(j)
    for f in range(K):
        for k in range(1,N):
            lst[k]+=lst[k-1]
    print(lst[N-1])
