import sys
input=sys.stdin.readline
lst1=[]
lst2=[]
lst3=[]
M=0
m=0
n=int(input())
cnt={}
for i in range(n):
    lst1.append(int(input()))
lst1=sorted(lst1)
M=sum(lst1)/n
if M-round(M)==0.5:
    M=+1
else:
    M=round(M)
print(M)

M=lst1[len(lst1)//2]
print(M)

for i in lst1:
    if i not in cnt:
        cnt[i]=1
    else:
        cnt[i]+=1
A=max(cnt.values())
for key, value in cnt.items():
    if value == A:
        lst3.append(key)
if len(lst3)>1:
    lst3.remove(min(lst3))

print(min(lst3))
M=max(lst1)
m=min(lst1)
print(M-m)


