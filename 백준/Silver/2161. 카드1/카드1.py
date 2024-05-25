from collections import deque
import sys
input =sys.stdin.readline
N= int(input())
lst1=deque([])

for i in range(1,N+1):
    lst1.append(i)
while len(lst1)!=0:
    print(lst1[0],end=" ")
    del lst1[0]
    lst1.rotate(-1)
