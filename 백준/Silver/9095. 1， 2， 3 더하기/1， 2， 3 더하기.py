import sys
input=sys.stdin.readline
lst2=[]
N=int(input())
for i in range(N):
    T=int(input())
    lst2.append(T)
max_value=max(lst2)
lst1=[0]*(max_value+1)
lst1[1]=1
lst1[2]=2
lst1[3]=4
n=4
while max_value+1!=n:
   lst1[n]=lst1[n-1]+lst1[n-2]+lst1[n-3]
   n+=1
for i in lst2:
    print(lst1[i])