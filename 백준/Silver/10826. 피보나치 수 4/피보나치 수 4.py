import sys
input=sys.stdin.readline
N=int(input())
result1=1
result2=1
temp=0
if(N==0):
    print(0)
elif(N==1 or N==2):
    print(1)
else:
    for i in range(N-2):
        temp=result2
        result2+=result1
        result1=temp
    print(result2)


