import sys
input =sys.stdin.readline
A,B=map(int,input().split())
A,B=A-1,B-1
U=1
D=1
for i in range(B):
    D*=B
    B-=1
    U*=A
    A-=1
print(U//D)