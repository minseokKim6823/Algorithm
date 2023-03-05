N=int(input())
A=[int(a) for a in input().split()]
M=int(input())
B=[int(a) for a in input().split()]
C=set(A)
D=set(B)
E=C&D
E=list(E)
B=list(B)
F=[]
for i in B:
    if i in E:
        print(1)
    else:
        print(0)
