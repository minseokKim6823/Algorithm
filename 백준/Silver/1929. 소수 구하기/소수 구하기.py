def Prime(m,n):
    nlst=[True]*(n+1)
    for i in range(2, int(n**0.5)+1):
        if nlst[i]==True:
            for j in range(i*2, n+1, i):
                nlst[j]=False
    for i in range(m, n+1):
        if nlst[i]==True and i!=1:print(i)


a,b=map(int, input().split())
Prime(a,b)