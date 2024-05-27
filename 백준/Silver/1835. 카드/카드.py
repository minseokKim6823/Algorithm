import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
lst=[0 for i in range(N)]
deq=deque([int(i) for i in range(N)])
cnt=1
while len(deq)!=0:
    for i in range(cnt):
        deq.rotate(-1)
    lst[deq[0]]=cnt
    del deq[0]
    cnt+=1
for i in range(len(lst)):
    print(lst[i], end=" ")