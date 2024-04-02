T=int(input())
for _ in range(T):
    q = 0
    d = 0
    n = 0
    p = 0
    c=int(input())
    while c!=0:
        if c>=25:
            q = c // 25
            c = c % 25
        elif c>=10:
            d = c // 10
            c %= 10
        elif c>=5:
            n = c // 5
            c %= 5
        else:
            p=c
            c=0
    print(q,d,n,p)