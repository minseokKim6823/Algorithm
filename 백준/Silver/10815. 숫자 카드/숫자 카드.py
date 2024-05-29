import sys
from collections import deque
input =sys.stdin.readline
N=int(input())
lst=list(map(int,input().split()))
M=int(input())
lst1=list(map(int,input().split()))

_dict = {}  # 속도는 dictionary!
for i in range(len(lst)):
    _dict[lst[i]] = 0  # 아무 숫자로 mapping

for j in range(M):
    if lst1[j] not in _dict:
        print(0, end=' ')
    else:
        print(1, end=' ')