import sys
input = sys.stdin.readline
N=int(input())
T=1000-N
lst=[500,100,50,10,5,1]
cnt=0
f=0
while T!=0:
    if T//lst[f]>=1:
        cnt+=T//lst[f]
        T=T%lst[f]
    f+=1
print(cnt)
