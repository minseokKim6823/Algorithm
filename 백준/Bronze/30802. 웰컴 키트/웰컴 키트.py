N=int(input())
lst=[int(i) for i in input().split()]
A,B=map(int,input().split())
hap=0
for i in range(len(lst)):
    max = 0
    if lst[i]%A!=0:
        if max<lst[i]//A:
            max=lst[i]//A
        max+=1
        hap+=max
    else:
        if max<lst[i]//A:
            max=lst[i]//A
        hap += max
print(hap)
print(N//B,end =" ")
print(N-B*(N//B))
