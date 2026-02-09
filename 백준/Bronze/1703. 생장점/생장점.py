while True:
    lst = list(map(int,input().split()))
    if len(lst) == 1:
        if lst[0] == 0:
            exit()
    result=lst[1]
    for i in range(2,len(lst)):
        if i%2==0:
            result -= lst[i]
        else:
            result *= lst[i]
        
    print(result)