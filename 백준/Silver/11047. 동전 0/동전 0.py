N,K =map(int, input().split())
lst=[]
A=0
T=K
min=100000000
for i in range(N):
    A=int(input())
    lst.append(A)

for i in range(len(lst)-1,-1,-1):
    result = 0
    K=T
    for j in range(i,-1,-1):
        if(lst[j]==K):
            result+=1
            K=0
            break
        elif(K>lst[j]):
            result+=K//lst[j]
            K=K%lst[j]
            if (result > min):
                break
        if (result > min):
            break
    if(result<min):
        min=result
print(min)

'''

1
5
10
50
100
500
1000
5000
10000
50000

'''