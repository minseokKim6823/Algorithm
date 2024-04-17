N=int(input())
lst=[int(i) for i in input().split()]
lst.sort(reverse=True)
result=0
cnt=1
for i in range(len(lst),0,-1):
    result+=lst[cnt-1]*cnt
    cnt+=1
print(result)