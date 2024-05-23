import sys
input =sys.stdin.readline
A=-1
cnt=0
while True:
    cnt+=1
    S = 0
    A,B,C=map(int,input().split())
    if A==0:
        break
    a=C//B
    b=C%B
    if A<b:
        b=A
    S=A*a+b
    print("Case",cnt,end="")
    print(":", S)
