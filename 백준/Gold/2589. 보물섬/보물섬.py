max=0
record=[0]*2500
list1=[]
alphabet=[]
h,w=map(int,input().split())
for i in range(h):
    list1.append(list(map(int,list(input().replace('W','0').replace('L','1')))))
checkcnt=1
for H in range(h):
    for W in range(w):
        cnt=0
        s=0
        e=0
        if(list1[H][W]>0):
            checkcnt=list1[H][W]
            record[e]=(H,W,1)
            e+=1
            list1[H][W]=checkcnt+1
        while(e>s):
                H1,W1,cnt=record[s]
                if(H1+1<h and list1[H1+1][W1]==checkcnt):
                    list1[H1+1][W1]=checkcnt+1
                    record[e]=(H1+1,W1,cnt+1)
                    e+=1
                if(H1-1>-1 and list1[H1-1][W1]==checkcnt):
                    list1[H1-1][W1]=checkcnt+1
                    record[e]=(H1-1,W1,cnt+1)
                    e+=1
                if(W1+1<w and list1[H1][W1+1]==checkcnt):
                    list1[H1][W1+1]=checkcnt+1
                    record[e]=(H1,W1+1,cnt+1)
                    e+=1
                if(W1-1>-1 and list1[H1][W1-1]==checkcnt):
                    list1[H1][W1-1]=checkcnt+1
                    record[e]=(H1,W1-1,cnt+1)
                    e+=1
                
                s+=1
        if(cnt>max):
            max=cnt
print(max-1)