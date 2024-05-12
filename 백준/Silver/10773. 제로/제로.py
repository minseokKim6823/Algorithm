import sys
input = sys.stdin.readline
lst=[]
N=int(input())
for i in range(N):
    num = int(input())
    if num!=0:
        lst.append(num)
    else:
        lst.pop()
print(sum(lst))