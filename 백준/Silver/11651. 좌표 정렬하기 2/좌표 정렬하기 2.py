lst1=[]
import sys
input = sys.stdin.readline
N=int(input())
for i in range(N):
    lst2=sys.stdin.readline().split()
    lst1.append(lst2)
lst1 = sorted (lst1, key=lambda x :[int(x[1]),int(x[0])])
for i in range(len(lst1)):
    for k in range(2):
        print(lst1[i][k],end=" ")
    print()



'''
5
3 4
1 1
1 -1
2 2
3 3
'''
