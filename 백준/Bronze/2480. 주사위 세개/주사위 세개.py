A,B,C=map(int,input().split())
prize=0
max=A
max2=0
max1=0
if A==B and B==C:
    prize=10000+A*1000
elif A==B or A==C:
    prize = 1000 + A * 100
elif C==B:
    prize = 1000 + B * 100
else:
    if(max<B):
        max1=B
        prize =B*100
    if(max<C):
        max2=C
    if(max2>max1):
        max=max2
        prize=max*100
    elif (max2 < max1):
        max = max1
        prize = max * 100
    else:
        prize=max*100
print(prize)