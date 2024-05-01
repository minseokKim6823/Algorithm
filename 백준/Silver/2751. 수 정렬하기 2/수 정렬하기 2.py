import sys
input = sys.stdin.readline
N=int(input())
lst1=[]
for i in range(N):
    lst1.append(int(input()))
lst1.sort()
for i in lst1:
    print(i)


'''
5
1
4
3
2
6
'''