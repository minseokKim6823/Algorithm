from collections import deque
def solution(board):
    n, m = len(board), len(board[0])
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False]*m for _ in range(n)]
    q = deque()
    
    for x in range(n):
        for y in range(m):
            if board[x][y] == "R":
                sx, sy = x, y
    
    q.append((sx, sy, 0))
    visited[sx][sy]=True
    
    while q:
        
        x, y, level = q.popleft()
        
        if board[x][y] == "G":
            return level
        
        # 한방향으로 미끄러져 이동
        for dx, dy in direction:
            nx,ny=x,y
            while 0<= nx+dx< n and 0<= ny+dy< m and board[nx+dx][ny+dy]!="D":
                nx+=dx
                ny+=dy
            
            if visited[nx][ny]==False:
                visited[nx][ny]=True
                q.append((nx,ny,level+1))
        
    return -1