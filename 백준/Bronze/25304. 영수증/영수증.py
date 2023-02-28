price=int(input())
su=int(input())
all=0
for i in range(su):
    a,b=map(int,input().split())
    all+=a*b
if(all==price):
    print("Yes")
else:
    print("No")