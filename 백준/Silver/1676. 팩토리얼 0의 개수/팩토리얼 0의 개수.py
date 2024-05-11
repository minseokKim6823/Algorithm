import sys
input=sys.stdin.readline
cnt=0
T=int(input())
def fac(N):
    if N==0 or N==1:
        return 1
    else:
        return N*fac(N-1)
su=str(fac(T))
for i in range(len(su) - 1, -1, -1):
    if su[i] == "0":
        cnt = cnt + 1
    else:
        print(cnt)
        break