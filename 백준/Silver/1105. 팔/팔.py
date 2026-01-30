L,R = map(str,input().split())
min=999999
cnt=0
flag=True
if len(L)!=len(R):
    print(0)
    exit()
for i in range(len(L)):
    if flag == True and L[i]!=R[i]:
        print(0)
        exit()
    elif flag == False and L[i]!=R[i]:
        print(cnt)
        exit()
    if L[i]=='8' and R[i]=='8':
        flag=False
        cnt+=1
print(cnt)