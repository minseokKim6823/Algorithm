import sys
from collections import deque

lst1=deque([])
input= sys.stdin.readline

def test(n):
    if n%1>=0.5:
        return int(n)+1
    else:
        return int(n)

N=int(input())
if N!=0:
    T=test(N*(15/100))
    for i in range(N):
        lst1.append(int(input()))

    lst1=sorted(lst1)
    lst1=deque(lst1)
    for i in range(T):
        lst1.pop()
        lst1.popleft()
    print(test(sum(lst1)/len(lst1)))
else:
    print(0)