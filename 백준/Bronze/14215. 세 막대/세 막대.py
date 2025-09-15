lst=[]
a,b,c=map(int,input().split())
lst.append(a)
lst.append(b)
lst.append(c)
max1=max(lst)
lst.remove(max1)
result=sum(lst)
if max1<sum(lst):
    result+=max1
else:
    result*=2
    result-=1
print(result)
