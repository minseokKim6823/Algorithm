import sys
N = int(sys.stdin.readline())
lst1=[]
for i in range(N):
    lst1.append(int(sys.stdin.readline()))
lst1= sorted(lst1,key=lambda x: x)
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