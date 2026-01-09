from collections import deque

n, m, start = map(int, input().split())


graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# print(graph)

for i in range(1, n + 1):
    graph[i].sort()

dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)
# print("graph : ", graph)
# print("dfs_visited : ", dfs_visited)
# print("bfs_visited : ", bfs_visited)

def dfs(v):
    dfs_visited[v] = True
    print(v, end=' ')
    for next_v in graph[v]:
        if not dfs_visited[next_v]:
            dfs(next_v)
def bfs(v):
    # print(v, end=' ')
    queue = deque([v])
    bfs_visited[v] = True
    while queue:
        # print("queue : ", queue)
        current = queue.popleft()
        print(current, end=' ')
        for next_v in graph[current]:
            if not bfs_visited[next_v]:
                bfs_visited[next_v] = True
                queue.append(next_v)


dfs(start)
print()
bfs(start)



