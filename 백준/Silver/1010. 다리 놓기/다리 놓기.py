import sys
input = sys.stdin.readline
def Factorial(n):
    if n==0:
        return 1;
    elif n==1:
        return 1;
    else:
        return n*Factorial(n-1)
T= int(input())
for i in range(T):
    A,B=map(int,input().split())
    a=Factorial(B)
    b=Factorial(A)
    c=Factorial(B-A)
    print(a//(b*c))