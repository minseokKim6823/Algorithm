from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque(range(1, N + 1))
result = []
print("<",end="")
while len(queue)!=1:
    queue.rotate(-(K-1))
    print(queue.popleft(),end=", ")
print(queue[0],end=">")