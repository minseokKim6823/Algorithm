num=int(input())
for i in range(num):
    avg = 0
    list1=[int(i) for i in input().split()]
    for k in range(1,len(list1)):
        avg+=list1[k]
        cnt = 0
    avg/=list1[0]
    for j in range(1,len(list1)):
        if(avg<list1[j]):
            cnt+=1
    print("{:.3f}".format(cnt/list1[0]*100)+"%")

'''
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50 
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

40.000%
57.143%
33.333%
66.667%
55.556%

'''