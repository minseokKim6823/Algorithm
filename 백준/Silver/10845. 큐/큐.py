import sys
N= int(sys.stdin.readline())
lst2=[]
for i in range(N):
    lst1= sys.stdin.readline().split()
    if lst1[0]=='push':
        lst2.append(lst1[1])
    elif lst1[0]== 'pop':
        if len(lst2)==0:
            print(-1)
        else:
            print(lst2[0])
            del lst2[0]
    elif lst1[0] =='front':
        if len(lst2) == 0:
            print(-1)
        else:
           print(lst2[0])
    elif lst1[0] =='back':
        if len(lst2)==0:
            print(-1)
        else:
            print(lst2[len(lst2)-1])
    elif lst1[0] == 'size':
        print(len(lst2))
    elif lst1[0] == 'empty':
        if len(lst2)==0:
            print(1)
        else:
            print(0)