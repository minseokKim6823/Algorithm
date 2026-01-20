from collections import deque
lst=[]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    field[y][x] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < M and 0 <= ny < N and field[ny][nx] == 1:
                field[ny][nx] = 0
                queue.append((nx, ny))


result=[]
T=int(input()) # 테스트 케이스
for i in range(T):
    M,N,K = map(int,input().split()) #가로,세로,배추위치
    cnt=0
    field=[[0 for i in range(M)] for i in range(N)]
    for i in range(K):
        x,y=map(int,input().split())
        field[y][x]=1
    count=0
    for x in range(M):
        for y in range(N):
            if field[y][x]==1:
                bfs(x,y)
                count+=1
    lst.append(count)

for i in lst:
    print(i)