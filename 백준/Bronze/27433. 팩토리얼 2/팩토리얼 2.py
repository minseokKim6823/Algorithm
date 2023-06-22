N=int(input())
t=1
if(N==0):
    t=1
else:
    for i in range(1,N+1):
        t*=i
print(t)