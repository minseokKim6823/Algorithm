from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst1=list(map(int,input().split()))
dq=deque([i for i in range(1, n+1)])
cnt=0
for value in lst1:
    while True:
        if dq[0]==value:
            dq.popleft()
            break
        else:
            if len(dq)/2>dq.index(value):
                while dq[0]!=value:
                    dq.rotate(-1)
                    cnt+=1
            else:
                while dq[0] != value:
                    dq.rotate(1)
                    cnt += 1
print(cnt)