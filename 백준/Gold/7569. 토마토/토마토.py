M,N,H=map(int,input().split())
list=[]
list1=[]
record=[]
a=[]
plus=0
plus1=0
t=True
for i in range(H):
    for j in range(N):
        list2=[int(k) for k in input().split()]
        list1.append(list2)
        list2=[]
    list.append(list1)
    list1=[]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if list[i][j][k]==1:
                record.append((i,j,k,1))
for i in range(H):
    for j in range(N):
        for k in range(M):
            if list[i][j][k]!=0:
                plus+=1
if(plus==H*N*M):
    print(0)
    t=False
    
for i in range(H):
    for j in range(N):
        for k in range(M):
            if list[i][j][k]==-1:
                plus1+=1
s=0
while s<len(record):
    i,j,k,day=record[s]
    if(i+1<H):
        if(list[i+1][j][k]==0):
            list[i+1][j][k]=1
            record.append((i+1,j,k,day+1))
    if(0<=i-1):
        if(list[i-1][j][k]==0):
            list[i-1][j][k]=1
            record.append((i-1,j,k,day+1))
    if(j+1<N):
        if(list[i][j+1][k]==0):
            list[i][j+1][k]=1
            record.append((i,j+1,k,day+1))
    if(0<=j-1):
        if(list[i][j-1][k]==0):
            list[i][j-1][k]=1
            record.append((i,j-1,k,day+1))
    if(k+1<M):
         if(list[i][j][k+1]==0):
            list[i][j][k+1]=1
            record.append((i,j,k+1,day+1))
    if(0<=k-1):
         if(list[i][j][k-1]==0):
            list[i][j][k-1]=1
            record.append((i,j,k-1,day+1))
    s+=1
if(len(record)==M*N*H-plus1 and t==True):
    print(record[len(record)-1][3]-1)
elif(len(record)<M*N*H-plus1 and t==True):
    print(-1)