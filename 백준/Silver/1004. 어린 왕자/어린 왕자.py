lst=[]
result=[]
n = int(input())
for _ in range(n):
    sx, sy, ex, ey = map(int, input().split())
    cnt=0
    m = int(input())
    for _ in range(m):
        x, y, r = map(int, input().split())
        if (x-sx)**2 + (y-sy)**2 <= r**2 or (x-ex)**2 + (y-ey)**2 <= r**2:
            if (x-sx)**2 + (y-sy)**2 <= r**2 and (x-ex)**2 + (y-ey)**2 <= r**2:
                pass
            else:
                cnt +=1
    lst.append(cnt)
for i in lst:
    print(i)