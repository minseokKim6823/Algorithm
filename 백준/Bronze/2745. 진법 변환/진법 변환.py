list1=[]
result=0
B,N=map(str,input().split())
N=int(N)
for i in range(10):
    list1.append(str(i))
for i in range(65,91):
    list1.append(chr(i))
for i in range(len(B)):
    result+=list1.index(B[i])*N**(len(B)-i-1)
print(result)