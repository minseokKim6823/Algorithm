list1=[int(i) for i in input().split()]
cnt=0
tnc=0
t=len(list1)-1
for i in range(t):
    if(list1[i]<list1[i+1]):
        cnt+=1
    else:
        tnc+=1
if cnt==t:
    print("ascending")
elif tnc==t:
    print("descending")
else:
    print("mixed")