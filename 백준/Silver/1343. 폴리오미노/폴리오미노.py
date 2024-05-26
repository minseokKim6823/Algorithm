board=input()
cnt=0
cnt1=-1
lst1=[]
t=0
while cnt1!=len(board):
    cnt1 += 1
    if cnt1==len(board):
        if cnt%2!=0:
            lst1 = []
            lst1.append(-1)
            break
        elif cnt%4==0:
            for i in range(cnt//4):
                lst1.append("AAAA")
        elif cnt%4==2:
            for i in range(cnt//4):
                lst1.append("AAAA")
            lst1.append("BB")
        cnt=0
    elif board[cnt1]=='.':
        if cnt%2!=0:
            lst1=[]
            lst1.append(-1)
            break
        elif cnt%4==0 and cnt!=0:
            for i in range(cnt//4):
                lst1.append("AAAA")
        elif cnt%4==2:
            for i in range(cnt//4):
                lst1.append("AAAA")
            lst1.append("BB")
        if cnt1!=len(board):
            lst1.append('.')
        cnt=0
    elif board[cnt1]=="X":
        cnt += 1
    if t==-1:
        break
for i in range(len(lst1)):
    print(lst1[i],end="")