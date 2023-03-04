num=int(input())
list1=[]
list3=[]
g=''
q=0
for i in range(num):
    t=0
    a, b = map(str, input().split())
    a = int(a)
    list2 = [0 for i in range(len(b)*a)]
    for j in range(len(b)):
        for k in range(a):
            list2[t]=b[j]
            t+=1
    list3.append(list2)
for i in range(num):
    if(q!=0):
        print("")
    for k in range(len(list3[i])):
        print(list3[i][k],end="")
        q+=1