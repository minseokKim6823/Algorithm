N = int(input())
list1=["long int"]
if(N==4):
    pass
else:
    t=int(N/4-1)
    for i in range(t):
        list1.append("long")
for i in range(len(list1)-1,-1,-1):
    print(list1[i],end =" ")