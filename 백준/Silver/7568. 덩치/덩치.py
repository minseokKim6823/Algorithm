import sys
input = sys.stdin.readline
N= int(input())
lst1=[]
for i in range(N):
    weight, height = map(int, input().split())
    lst1.append((weight, height))

for i in lst1:
    rank=1
    for j in lst1:
        if i[0]<j[0] and i[1]<j[1]:
            rank +=1
    print(rank,end=" ")

'''
5
50 200
55 185
58 183
88 186
60 175

1
3
3
1
3


2
100 100
100 200

1 1
'''