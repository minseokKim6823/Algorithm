X,Y=map(int,input().split())#X=7 Y=6
list=[[0 for i in range(X)]for k in range(Y)]
Z=int(input())
def start(X,Y,Z):
    x=0
    y=0
    sw=1
    cnt=1
    t=0
    while True:
        for i in range(Y):
            list[y][x]==cnt
            if(cnt==Z and t==0):
                print(x+1,y+1)
                t+=1
                break
            cnt+=1
            y+=sw
        if (t == 1):
            break
        y-=sw
        x+=sw
        X-=1
        Y-=1
        for i in range(X):
            list[y][x]=cnt
            if(cnt==Z and t==0):
                print(x+1,y+1)
                t += 1
                break
            cnt+=1
            x+=sw
        if (t == 1):
            break
        x-=sw
        y-=sw
        sw*=-1

if(X*Y<Z):
    print(0)
else:
    start(X,Y,Z)