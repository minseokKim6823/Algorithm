N,M = map(int,input().split())
lst=[int(i) for i in input().split()]
lst1=[]
result=[]
dif=10000000000000000
for i in range(len(lst)-2):
    for j in range(i+1,len(lst)-1):
            for k in range(j + 1, len(lst)):
                value = lst[k]+lst[j]+lst[i]
                if(M-value>=0):
                    t=M-value
                    if(dif>t):
                        dif=t
                        result=value
print(result)