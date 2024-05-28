import sys
input=sys.stdin.readline
T=int(input())
for i in range(T):
    a = 1
    b = 0
    N=int(input())
    for j in range(N):
        temp=b
        b=a+b
        a=temp
    print(a,b)