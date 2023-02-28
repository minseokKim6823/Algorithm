X,Y=map(int,input().split())
su=int(input())
list=[]
dis=0
min=0
H=X*2+Y*2
for i in range(su+1):
    list1=[int(i)for i in input().split()]
    if(list1[0]==1):
        list1[0]=0
    elif(list1[0]==2):
        list1[0]=Y
    elif(list1[0]==3):
        list1[0]=list1[1]
        list1[1]=0
    elif(list1[0]==4):
        list1[0]=list1[1]
        list1[1]=X
    list.append(list1)
list.pop(su)
for i in range(su):
    for k in range(2):
        if(list1[0]==Y and list[i][0]==0):
            L=list1[1]+list1[0]+list[i][0]+list[i][1]
            min=H-L
            if(min>L):
                min=L
            dis=dis+min/2
            T=L
            L=0
        elif(list1[0]==0 and list[i][0]==Y):
            L=list1[1]+list1[0]+list[i][0]+list[i][1]
            min=H-L
            if(min>L):
                min=L
            dis=dis+min/2
            T=L
            L=0
        elif(list1[1]==X and list[i][1]==0):
            L=list1[1]+list1[0]+list[i][0]+list[i][1]
            min=H-L
            if(min>L):
                min=L
            dis=dis+min/2
            T=L
            L=0
        elif(list1[1]==0 and list[i][1]==X):
            L=list1[1]+list1[0]+list[i][0]+list[i][1]
            min=H-L
            if(min>L):
                min=L
            dis=dis+min/2
            T=L
            L=0
        else:
            if(list[i][k]-list1[k]<0):
                L=(list[i][k]-list1[k])*-1
                dis=dis+L
                L=0
            else:
                L=list[i][k]-list1[k]
                dis=dis+L
             
print(int(dis))