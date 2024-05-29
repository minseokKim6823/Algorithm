import sys
input =sys.stdin.readline
T=int(input())
s=set()
for i in range(T):
    lst1 = list(input().split())
    if lst1[0]=="add":
        if lst1[1] not in s:
            s.add(lst1[1])
    elif lst1[0]=="remove":
        if lst1[1] in s:
            s.remove(lst1[1])
    elif lst1[0]=="check":
        if lst1[1] in s:
            print(1)
        else:
            print(0)
    elif lst1[0] == "toggle":
        if lst1[1] in s:
            s.remove(lst1[1])
        else:
            s.add(lst1[1])
    elif lst1[0] == "all":
        s = set([str(i) for i in range(1, 21)])
    elif lst1[0] == "empty":
        s=set()