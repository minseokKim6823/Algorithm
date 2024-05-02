import sys
input = sys.stdin.readline
N,K = map(int,input().split())
def fac(n):
    if n==1:
        return 1
    else:
        return n * fac(n-1)
if K ==0 or K==N:
    print(1)
else:
    print(int(fac(N)/(fac(N-K)*fac(K))))