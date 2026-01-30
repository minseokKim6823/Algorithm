import math
T=int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d1 = ((x1-x2)**2)+((y1-y2)**2)
    d2 = (r1+r2) ** 2
    d3 = (r2-r1) ** 2

    if x1==x2 and y1 ==y2 and r1==r2:
        print(-1)
    elif d1 == d2:
        print(1)
    elif d1==d3:
        print(1)
    elif d1 > d2:
        print(0)
    elif d1 < d3:
        print(0)
    else:
        print(2)
    