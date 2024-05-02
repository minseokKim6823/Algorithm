from collections import deque
import sys
input =sys.stdin.readline
N=int(input())
lst1=deque([int(i+1) for i in range(N)])
while len(lst1)!=1:
    del lst1[0]
    lst1.rotate(-1)
print(lst1[0])