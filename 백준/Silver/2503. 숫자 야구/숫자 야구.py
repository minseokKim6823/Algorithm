H=int(input())
list=[]
lists=[]
for a in range(H):
    list+=[int(a) for a in input().split()]
for b in range(100,1000):
    s = str(b)
    if (int(s[1]) != 0 and int(s[2]) != 0 and int(s[0]) != int(s[1]) and int(s[0]) != int(s[2]) and int(s[1]) != int(
            s[2])):
        cnt=0
        for n in range(H):#H=4
            cnts=0
            cntb=0
            t=str(list[3*n])
            for i in range(3):
                if(s[i]==t[i]):
                    cnts+=1
                elif(s[i] in t):
                    cntb+=1
            if(list[3*n+1]==cnts):
                if(list[3*n+2]==cntb):
                    cnt+=1
        if cnt==H:
            lists.append(b)
print(len(lists))