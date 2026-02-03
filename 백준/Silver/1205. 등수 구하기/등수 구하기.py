A,B,C = map(int,input().split())
if A==0:
    print(1)
    exit()
lst = list(map(int,input().split()))
if A==C:
    if lst[len(lst)-1] >= B:
        print(-1)
    else:
        lst.append(B)
        lst.sort(reverse=True)
        print(lst.index(B)+1)
else:
    lst.append(B)
    lst.sort(reverse=True)
    print(lst.index(B)+1)
