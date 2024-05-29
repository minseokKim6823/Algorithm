import sys
input =sys.stdin.readline
N=int(input())
A,B=1,1
for i in range(N-1):
    A,B=B,A+B
print(A*2+B*2)