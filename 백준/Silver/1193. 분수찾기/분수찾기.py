N=int(input())
t=0
p=1
result=0
while N>result:
   t+=1
   p+=1
   result1=result
   result+=t
if(p%2==1):
    print(N-result1,end="")
    print("/",end="")
    print(p-(N-result1))
else:
    print(p - (N - result1), end="")
    print("/", end="")
    print(N - result1)
