list = []
list2=[]
r_cnt = 0
su=0
c_cnt=0
lc_cnt=0
h_cnt = 0
w_cnt =0
a=0
Q=0
for i in range(5):
    list1 = [int(k) for k in input().split()]
    list += list1
for i in range(5):
    list22 = [int(k) for k in input().split()]
    list2 += list22
for i in range(5):
    for k in range(5):
        ad = list.index(list2[k+i*5])
        su=list[ad]
        list[ad] =0 # 사회자가 말한 숫자를 0으로 바꾼다
        Q+=1
        for z in range(1,6):
            if list[4*z]==0:
                c_cnt+=1
                if c_cnt == 5:
                    r_cnt += 1
                    c_cnt = 0
        for t in range(5):
            if list[6*t]==0:
                lc_cnt+=1
                if lc_cnt==5:
                    r_cnt+=1
                    lc_cnt = 0
        for j in range(5):
            h_cnt=0
            w_cnt=0
            for l in range(5):
                if (list[l * 5 + j] == 0): #세로
                    h_cnt += 1
                if (h_cnt == 5):
                    r_cnt += 1
                    h_cnt = 0
            for y in range(5):
                if (list[5 * j + y] == 0):  # 가로
                    w_cnt += 1
                if (w_cnt == 5):
                    r_cnt += 1
                    w_cnt = 0
        if(r_cnt<3):
            r_cnt = 0
            c_cnt = 0
            lc_cnt = 0
            h_cnt = 0
            w_cnt = 0
        else:
            q=int(Q)
            print(q)
            break
    if(r_cnt>=3):
        break







'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''