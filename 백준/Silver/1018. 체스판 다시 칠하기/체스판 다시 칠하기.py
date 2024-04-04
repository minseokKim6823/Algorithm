lst1=['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
lst2=['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
N,M=map(int,input().split())
lst=[]
min=64
t=1
p=0
for i in range(N):
    color=input()
    lst.append(color)
for i in range(N-7):#세로
    for j in range(M-7):#가로
        cnt1 = 0
        cnt2 = 0
        if lst[i][j] == 'B':
            for a in range(i,i+8):#세로
                for b in range(j,j+8):#가로

                    if(lst[a][b]!=lst1[a-i][b-j]):
                        cnt1+=1
                    if(lst[a][b]!=lst2[a-i][b-j]):
                        cnt2+=1

            if(cnt1<=cnt2 and cnt1<=min):
                min=cnt1
            elif(cnt1>=cnt2 and cnt2<=min):
                min=cnt2

        if lst[i][j] == 'W':
            for a in range(i, i + 8):  # 세로
                for b in range(j, j + 8):  # 가로
                    if (lst[a][b] != lst1[a-i][b-j]):
                        cnt1 += 1
                    if (lst[a][b] != lst2[a-i][b-j]):
                        cnt2 += 1

            if (cnt1 <=cnt2 and cnt1 <= min):
                min = cnt1
            elif (cnt1 >= cnt2 and cnt2 <= min):
                min = cnt2
print(min)


