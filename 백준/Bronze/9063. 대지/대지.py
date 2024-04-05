T = int(input())
minx=10001
maxx=-10001
miny=10001
maxy=-10001
lst=[]
for i in range(T):
    lst.append(list(map(int, input().split())))
if len(lst) == 1:
    S = 0
else:
    for i in range(len(lst)):
        if minx>lst[i][0]:
            minx=lst[i][0]
        if maxx<lst[i][0]:
            maxx=lst[i][0]
        if miny>lst[i][1]:
            miny = lst[i][1]
        if maxy<lst[i][1]:
            maxy = lst[i][1]
if maxy==-10001:
    print(S)
else:
    if minx==maxx or miny==maxy:
        print(0)
    else:
        print((maxx-minx)*(maxy-miny))