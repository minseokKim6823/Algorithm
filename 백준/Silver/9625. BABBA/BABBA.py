N=int(input())
A=1
B=0
for i in range(N):
    tmp=A
    A=B
    B=tmp+B
print(A,B)