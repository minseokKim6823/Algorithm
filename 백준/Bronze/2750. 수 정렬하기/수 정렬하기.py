lst=[]
cnt=int(input())
for i in range(cnt):
    num=int(input())
    lst.append(num)
lst=sorted(lst)
for i in range(len(lst)):
    print(lst[i])