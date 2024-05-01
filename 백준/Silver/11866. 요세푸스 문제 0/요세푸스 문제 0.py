import sys
input = sys.stdin.readline

lst=[]
lst1=[]
N,K= map(int,input().split())
K-=1
T=K
for i in range(1,N+1):
    lst.append(i)
for i in range(N):
    if K>=len(lst):
        K= K%len(lst)
    if K<len(lst):
        lst1.append(lst[K])
        del lst[K]
        K+=T
print("<",end="")
for i in range(len(lst1)-1):
    print(lst1[i],end=", ")
print(lst1[len(lst1)-1],end="")
print(">")

'''
<7, 1, 3, 6, 2, 4, 5>
'''