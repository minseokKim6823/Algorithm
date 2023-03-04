g=1
for i in range(3):
    su=int(input())
    g*=su
list1=[0 for i in range(10)]
g=str(g)
for i in range(len(g)):
    t=g[i]
    t=int(t)
    list1[t]+=1
for i in range(len(list1)):
    print(list1[i])