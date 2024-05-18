from collections import deque
import sys
input = sys.stdin.readline
idx=0
lst1=[]
stack1=deque([])
stack2=deque([])
N=int(input())
for i in range(N):
    stack1.append(int(input()))

stack2.append(1)
lst1.append("+")
t=1
while len(lst1)!=0:
    if len(stack2)==0 or stack2[len(stack2)-1]<stack1[idx]:
        t+= 1
        stack2.append(t)
        lst1.append("+")
    elif stack2[len(stack2)-1] == stack1[idx]:
        del stack1[idx]
        lst1.append("-")
        stack2.pop()
    elif stack2[len(stack2)-1] > stack1[idx]:
        lst1.append("NO")
        break
    if len(stack1) == 0:
        break
if "NO" in lst1:
    print("NO")
else:
    for i in lst1:
        print(i)

'''
5
1
2
5
4
3
'''