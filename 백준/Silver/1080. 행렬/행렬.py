def flip(i, j):
            for x in range(i, i+3):
                for y in range(j, j+3):
                    lst1[x][y] = '1' if lst1[x][y] == '0' else '0'
count=0
N, M = map(int, input().split())
lst1 = [list(input().strip()) for _ in range(N)]
lst2 = [list(input().strip()) for _ in range(N)]
if N<3 or M<3:
    if(lst1 == lst2):
        print(0)
    else:
        print(-1)
    exit()
for i in range(N-2):
    for j in range(M-2):
        if lst1[i][j] != lst2[i][j]:
            flip(i, j)
            count+=1
if(lst1 == lst2):
    print(count)
else:
    print(-1)
