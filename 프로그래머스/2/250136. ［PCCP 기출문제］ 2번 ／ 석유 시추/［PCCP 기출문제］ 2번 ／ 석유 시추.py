from collections import deque

def solution(land):
    ny, nx = len(land), len(land[0])  # 행, 열 순서 맞추기
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    result1 = [0 for _ in range(nx)]
    visited = set()  # 리스트 대신 set 사용

    def bfs(x, y):
        cnt = 0  # 덩어리 크기 카운트
        q = deque()
        q.append((x, y))
        visited.add((y, x))  # 방문 처리 (y, x 순서로 저장)
        min_x, max_x = x, x  # 해당 덩어리의 x 범위

        while q:
            cx, cy = q.popleft()
            cnt += 1  # 1개 셀 포함
            
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= ny < len(land) and 0 <= nx < len(land[0]) and (ny, nx) not in visited and land[ny][nx] == 1:
                    q.append((nx, ny))
                    visited.add((ny, nx))
                    min_x = min(min_x, nx)
                    max_x = max(max_x, nx)

        for i in range(min_x, max_x + 1):
            if 0 <= i < len(result1):  # 인덱스 초과 방지
                result1[i] += cnt  

    # 모든 위치에서 BFS 실행
    for y in range(ny):
        for x in range(nx):
            if (y, x) not in visited and land[y][x] == 1:
                bfs(x, y)

    return max(result1)
