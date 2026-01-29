import math
xa,ya,xb,yb,xc,yc=map(int,input().split())
lst=[]
lst1=[xa,ya]
lst2=[xb,yb]
lst3=[xc,yc]

def length(lstA,lstB,lstC):
    if (lstA[0]==lstB[0] and lstA[0]==lstC[0]) or (lstA[1]==lstB[1] and lstA[1]==lstC[1]):
        print(-1.0)
        exit()
    elif (lstB[0]-lstA[0])!= 0 and (lstC[0]-lstA[0])!= 0 and (lstB[1]-lstA[1])/(lstB[0]-lstA[0]) == (lstC[1]-lstA[1])/(lstC[0]-lstA[0]):
        print(-1.0)
        exit()
    else:
        BC=math.sqrt((lstB[0]-lstC[0])**2+(lstB[1]-lstC[1])**2)
        BA=math.sqrt((lstB[0]-lstA[0])**2+(lstB[1]-lstA[1])**2)
        value = BC * 2 + BA * 2
        if value not in lst:
            lst.append(value)
        CA = math.sqrt((lstC[0] - lstA[0]) ** 2 + (lstC[1] - lstA[1]) ** 2)
        CB = math.sqrt((lstC[0] - lstB[0]) ** 2 + (lstC[1] - lstB[1]) ** 2)
        value = CA * 2 + CB * 2
        if value not in lst:
            lst.append(value)

        AC = math.sqrt((lstA[0] - lstC[0]) ** 2 + (lstA[1] - lstC[1]) ** 2)
        AB = math.sqrt((lstA[0] - lstB[0]) ** 2 + (lstA[1] - lstB[1]) ** 2)
        value = AC * 2 + AB * 2
        if value not in lst:
            lst.append(value)

for i in range(3):
    if i==0:
        length(lst1,lst2,lst3)
    elif i==1:
        length(lst2,lst1,lst3)
    else:
        length(lst3,lst1,lst2)
print(max(lst)-min(lst))
