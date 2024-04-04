N=int(input())
c=0
if N==4 or N==7:
    print(-1)
elif N==3 or N==5:
    print(1)
elif N==8 or N==6:
    print(2)
elif N==11 or N==9 or N==13:
    print(3)
elif N==12 or N==14:
    print(4)
elif N==17:
    print(5)
else:
    lst = []
    T=N//5
    for i in range(1,T+1):
        a=N//(5*i)
        b=N-5*i
        if(b!=0):
            c=b//3
        if b%3!=0:
            if -1 not in lst:
                lst.append(-1)
        else:
            lst.append(i+b//3)
    if lst[0]==-1 and len(lst)==1:
        print(-1)
    elif -1 in lst:
        lst.remove(-1)
        print(min(lst))


