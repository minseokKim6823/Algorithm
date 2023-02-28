N, L, F = map(int, input().split())#모눈종이 크기,그물길이,물고기위치
list1 = []
list2 = []
listx = [0 for i in range(N)]
listy = [0 for i in range(N)]
max = 0
for i in range(F):
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    list1.append([x, y])
    listx[x] += 1
    listy[y] += 1
for x in range(N):
    if (listx[x] != 0):
        for y in range(N):
            if (listy[y] != 0):
                list2.append([x, y])
for k in range(len(list2)):
    x = list2[k][0]
    y = list2[k][1]
    for i in range(1,L//2):
        cnt = 0
        w = i #그물 가로
        h = L//2 - w #그물 세로
        X = x + w
        Y = y + h
        for c in range(len(list1)):
            if (x<=list1[c][0]<=X and y<=list1[c][1]<=Y):
                cnt += 1
                if (max < cnt):
                    max = cnt

print(max)

'''
7 10 6 
2 2 
2 4 
6 2 
7 4 
3 3 
5 6
'''
























'''list2=[]
list1=[[0 for i in range(N)]for i in range(N)]
for i in range(F):
    y,x=map(int,input().split())
    y-=1
    x-=1
    list1[y][x]=1
    list2.append([y,x])
for i in range(F):'''

