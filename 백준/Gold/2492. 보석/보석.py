list1=[]
list2=[]
listW=[]
listH=[]
max=0
cnt=0
N,M,T,K=map(int,input().split())#N너비M높이T금강석 개수K정사각형 한 변 길이
#너비N=10 높이M=6 갯수T=7 K=3
listW=[]
listH=[]
list2=[0 for i in range(T)]
for i in range(T):
    list1=[int(k) for k in input().split()]
    num1=list1[0]
    num2=list1[1]
    listW.append(num1)
    listH.append(num2)
    list2[i]=list1
list1=[]
listW.append(0)
listH.append(0)
for i in listW:
    x=i
    for k in listH:
        y=k
        list1.append([x,y])
for k in range(len(list1)):

    x=list1[k][0]
    y=list1[k][1]
    X=x+K
    Y=y+K
    cnt = 0
    if X<=N and Y<=M:
        for i in range(len(list2)):
            if(x<=list2[i][0]<=X and y<=list2[i][1]<=Y):
                cnt+=1
                if(cnt>=max):
                    max=cnt
                    maxX = x
                    maxY = Y
    X = x - K
    Y = y + K
    cnt = 0
    if X >=0 and Y <= M:
        for i in range(len(list2)):
            if (X <= list2[i][0] <= x and y <= list2[i][1] <= Y):
                cnt += 1
                if (cnt >= max):
                    max = cnt
                    maxX = X
                    maxY = Y
    X = x + K
    Y = y - K
    cnt = 0
    if X <= N and Y >=0:
        for i in range(len(list2)):
            if (x <= list2[i][0] <= X and Y <= list2[i][1] <= y):
                cnt += 1
                if (cnt >= max):
                    max = cnt
                    maxX = x
                    maxY = y
    X = x - K
    Y = y - K
    cnt = 0
    if X >=0 and Y >=0:
        for i in range(len(list2)):
            if (X <= list2[i][0] <= x and Y <= list2[i][1] <= y):
                cnt += 1
                if (cnt >= max):
                    max = cnt
                    maxX = X
                    maxY = y

print(maxX,maxY)
print(max)


'''
10 6 7 3
2 2
3 4
7 6
4 5
4 3
5 3
6 4
'''
'''
for i in range(M):
    if(listW[i]!=0):
        if(minW>i):
            minW=i
        if(maxW<i):
            maxW=i
for i in range(N):
    if(listH[i]!=0):
        if(minH>i):
            minH=i
        if(maxH<i):
            maxH=i
'''