N=int(input())
lst1=[0 for i in range(N+1)]
for i in range(2,N+1):
    lst1[i]=lst1[i-1]+1
    if i%2==0:
        lst1[i] =min(lst1[i],lst1[i//2]+1)
    if i%3==0:
        lst1[i] = min(lst1[i], lst1[i // 3] + 1)
print(lst1[N])