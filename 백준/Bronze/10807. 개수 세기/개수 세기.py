num=int(input())
list1=[int(i) for i in input().split()]
v=int(input())
cnt=0
for i in range(num):
    if v in list1:
        list1.remove(v)
        cnt+=1
        if(len(list1)==0):
            print(cnt)
    else:
        print(cnt)
        break